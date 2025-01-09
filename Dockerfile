FROM python:3.11.6-slim

WORKDIR /src

RUN apt-get update && apt-get install -y \
    software-properties-common \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY . /app

WORKDIR /app/src

CMD  ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000"]