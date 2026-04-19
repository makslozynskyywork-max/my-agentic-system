# Базуємось на офіційному образі OpenClaw
FROM ghcr.io/openclaw/openclaw:latest

USER root

# Додаємо Python та Git (обробляємо як Alpine, так і Debian бази)
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv git || \
    (apk update && apk add python3 py3-pip git)

# Створюємо віртуальне середовище, щоб уникнути помилок pip break-system-packages
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Встановлюємо MemPalace
RUN git clone https://github.com/mempalace/mempalace.git /opt/mempalace
WORKDIR /opt/mempalace
RUN pip install --no-cache-dir -e .

WORKDIR /app
