from fastapi import FastAPI, Request, BackgroundTasks
import uvicorn
import docker
import os
import json

app = FastAPI()

# Connect to the docker socket mounted from host
client = docker.from_env()

# Get configured image or fallback
IMAGE_NAME = os.getenv("OPENCLAW_IMAGE", "local-openclaw-with-mempalace")

def spawn_openclaw_worker(agent_id: str, role: str, task: str):
    """
    Background worker that spins up an ephemeral OpenClaw docker container.
    """
    print(f"Spawning OpenClaw for Wing: {role}, Task: {task}")
    try:
        container = client.containers.run(
            IMAGE_NAME,
            command=[
                "--non-interactive",
                "--task", task,
                "--mcp-server", "python3 -m mempalace.mcp_server", # Direct internal execution!
                "--wing", role
            ],
            environment={
                "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY", "")
            },
            network_mode="system_agent_internal_net", # Attach to isolated VPS network
            volumes={
                "system_mempalace_data": {"bind": "/root/.mempalace", "mode": "rw"} # Share global memory natively!
            },
            detach=True,
            remove=True # Auto-cleanup when done
        )
        print(f"Container created with ID: {container.id}")
    except Exception as e:
        print(f"Error spawning OpenClaw instance: {str(e)}")


@app.post("/invoke")
async def invoke_agent(request: Request, background_tasks: BackgroundTasks):
    """
    Endpoint that Paperclip webhook hits when delegating a task to an agent.
    """
    payload = await request.json()
    
    # Extract agent definitions from payload
    # Note: paperclip adapters usually send {"agentId": "...", "role": "...", "task": "..."}
    agent_id = payload.get("agentId", "default_agent")
    role = payload.get("role", "Worker")
    task = payload.get("task", "Awaiting configuration or task...")
    
    # Send actual execution to background to avoid blocking paperclip webhook
    background_tasks.add_task(spawn_openclaw_worker, agent_id, role, task)
    
    return {"status": "accepted", "message": f"Worker {agent_id} spawning..."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
