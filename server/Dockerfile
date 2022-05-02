FROM python:3.8

# 

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

ENV DOCKER_CLIENT_VERSION=1.12.3
ENV DOCKER_API_VERSION=1.24
RUN curl -fsSL https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_CLIENT_VERSION}.tgz \
    | tar -xzC /usr/local/bin --strip=1 docker/docker

#

# コンテナ内で必要なパッケージをインストール
WORKDIR /app
COPY /app/requirements.txt .
RUN pip install -r requirements.txt

# __pycache__
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
EXPOSE 8000
# FastAPIを8000ポートで待機
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]