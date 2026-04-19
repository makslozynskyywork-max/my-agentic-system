$ErrorActionPreference = "Stop"

Write-Host "Cloning repositories for Unified AI Agent System..."

# 1. Paperclip
if (-not (Test-Path "paperclip")) {
    Write-Host "Cloning Paperclip..."
    git clone https://github.com/paperclipai/paperclip.git
} else {
    Write-Host "Paperclip already cloned."
}

# 2. OpenClaw
if (-not (Test-Path "openclaw")) {
    Write-Host "Cloning OpenClaw..."
    git clone http://github.com/openclaw/openclaw.git
} else {
    Write-Host "OpenClaw already cloned."
}

# 3. MemPalace
if (-not (Test-Path "mempalace")) {
    Write-Host "Cloning MemPalace..."
    git clone https://github.com/mempalace/mempalace.git
} else {
    Write-Host "MemPalace already cloned."
}

Write-Host "Done! All repositories downloaded."
