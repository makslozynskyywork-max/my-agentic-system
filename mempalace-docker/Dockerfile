FROM python:3.11-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Clone the repository provided by the user
RUN git clone https://github.com/mempalace/mempalace.git /app

WORKDIR /app

# Install dependencies and mempalace module
RUN pip install --no-cache-dir -e .

# Expose standard MCP Server port
EXPOSE 5000

# Start MCP Server
CMD ["python3", "-m", "mempalace.mcp_server", "--host", "0.0.0.0", "--port", "5000"]
