# Todo-CICD Project – Step-by-Step Flow

This document outlines the complete workflow for setting up the Todo-CICD project, from creating the project folder, developing the app, preparing Docker, and pushing to GitHub.

## 1️⃣ Create Project Folder




mkdir C:\Users\ADMIN\Downloads\todo-cicd
cd C:\Users\ADMIN\Downloads\todo-cicd
## 2️⃣ Create the App

Inside the folder, create your Python application:

todo-cicd/
├── app/
│   └── main.py

# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Todo-CICD app running!"}

## 3️⃣ Create Requirements File

Add a requirements.txt for dependencies:

fastapi
uvicorn

Install locally to test:

pip install -r requirements.txt

## 4️⃣ Dockerize the Application

Create a Dockerfile in the project folder:

# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Build the Docker image:

docker build -t todo-app .
Run the container:
docker run -d -p 8000:8000 todo

## 5️⃣ Initialize Git & Push to GitHub
create an new repo
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/todo-cicd.git
git push -u origin main




    A[Create Project Folder: todo-cicd] --> B[Create App Backend: app/main.py]
    B --> C[Add Dependencies: requirements.txt]
    C --> D[Dockerize App: Dockerfile]
    D --> E[Build & Run Docker Container]
    E --> F[Access App in Browser: http://localhost:8000]
    F --> G[Initialize Git]
    G --> H[Stage & Commit Files]
    H --> I[Rename Branch to main]
    I --> J[Add Remote GitHub Repo]
    J --> K[Push to GitHub]
# Test push - secrets should load now