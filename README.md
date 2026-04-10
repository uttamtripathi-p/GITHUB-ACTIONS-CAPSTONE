# 🐳 Dockerized Flask Todo

A fully containerized Todo web application built with Python Flask and MySQL, orchestrated with Docker Compose.
Built by Uttam Tripathi as part of a DevOps learning journey.

## CI/CD Status

![Main Branch Pipeline](https://github.com/uttamtripathi-p/GITHUB-ACTIONS-CAPSTONE/actions/workflows/main-pipeline.yml/badge.svg)
![Health Check](https://github.com/uttamtripathi-p/GITHUB-ACTIONS-CAPSTONE/actions/workflows/health-check.yml/badge.svg)

## Docker Hub

[![Docker Pulls](https://img.shields.io/docker/pulls/uttamtripathi/github-actions-capstone)](https://hub.docker.com/r/uttamtripathi/github-actions-capstone)
[![Docker Image Size](https://img.shields.io/docker/image-size/uttamtripathi/github-actions-capstone/latest)](https://hub.docker.com/r/uttamtripathi/github-actions-capstone)

Pull the image directly:

```bash
docker pull uttamtripathi/github-actions-capstone:latest
```

## Preview

A glassmorphism-themed Todo app where you can:
* ✅ Add todos
* ❌ Delete todos
* 💾 Data persists in MySQL even after container restarts

## Tech Stack

| Layer | Technology |
|---|---|
| Web App | Python Flask |
| Database | MySQL 8.0 |
| Containerization | Docker |
| Orchestration | Docker Compose |
| CI/CD | GitHub Actions |
| Styling | Glassmorphism CSS |

## Project Structure

​```
GITHUB-ACTIONS-CAPSTONE/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image for Flask app
├── docker-compose.yml      # Multi-container setup
├── conftest.py             # Pytest configuration
├── tests/
│   └── test_app.py         # Unit tests
├── .github/
│   └── workflows/
│       ├── main-pipeline.yml        # Main CI/CD pipeline
│       ├── health-check.yml         # Scheduled health check
│       ├── reusable-docker.yml      # Reusable build & push
│       └── reusable-build-test.yml  # Reusable build & test
└── .env                    # Environment variables (not committed)
​```

## Getting Started

### 1. Clone the repo

​```bash
git clone https://github.com/uttamtripathi-p/GITHUB-ACTIONS-CAPSTONE.git
cd GITHUB-ACTIONS-CAPSTONE
​```

### 2. Create .env file

​```
MYSQL_ROOT_PASSWORD=your_root_password
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=flaskdb
​```

### 3. Start the stack

​```bash
docker-compose up -d
​```

### 4. Create the todos table

​```bash
docker exec -it mysql mysql -u root -p
​```

Then inside MySQL:

​```sql
USE flaskdb;
CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL
);
​```

### 5. Access the app

Open your browser at:
​```
http://localhost:8080
​```

## Dockerfile

​```dockerfile
# Base image
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY . .

# Run the app
CMD ["python", "app.py"]
​```

## docker-compose.yml

​```yaml
services:
  web:
    build: .
    container_name: python-flask
    ports:
      - "8080:5000"
    environment:
      DB_HOST: db
      DB_USER: ${MYSQL_USER}
      DB_PASSWORD: ${MYSQL_PASSWORD}
      DB_NAME: ${MYSQL_DATABASE}
    networks:
      - mynetwork
    depends_on:
      db:
        condition: service_healthy

  db:
    image: mysql:8.0
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
    volumes:
      - myvolume:/var/lib/mysql
    networks:
      - mynetwork
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    restart: on-failure

volumes:
  myvolume:

networks:
  mynetwork:
​```

## CI/CD Pipeline

​```
push to master
      ↓
build-test ──┐
             ├──→ build-push ──→ deploy
prep ────────┘         ↓
                uttamtripathi/github-actions-capstone:latest
                uttamtripathi/github-actions-capstone:<sha>

every 12 hours
      ↓
health-check (pull → run → curl /health → cleanup → summary)
​```

## Key Concepts Applied

* Multi-container setup with Docker Compose
* Custom Dockerfile for Flask app
* Named volumes for MySQL data persistence
* Environment variables via .env file
* Healthchecks — app waits for DB to be truly ready
* Restart policy — MySQL restarts on failure
* Custom network for service isolation
* GitHub Actions CI/CD pipeline with reusable workflows
* Scheduled health checks every 12 hours
* Docker Hub image publishing with SHA tags

## Commands

​```bash
docker-compose up -d           # Start stack
docker-compose down            # Stop and remove containers
docker-compose up --build -d   # Rebuild after code changes
docker-compose logs web        # View Flask logs
docker-compose ps              # View running services
docker system df               # Check disk usage
​```

---
Built as part of a DevOps learning journey 🚀
