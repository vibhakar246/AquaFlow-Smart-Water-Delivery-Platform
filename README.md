🚰 AquaFlow – Smart Water Delivery Platform
DevOps CI/CD & AIOps Enabled Application

Author: Vibhakar Kumar

AquaFlow is a smart water can delivery application built to demonstrate a real-world DevOps CI/CD pipeline.
The platform processes WhatsApp-style order messages, calculates billing automatically, and showcases modern DevOps practices with AIOps integration.

This project is designed following company-standard DevOps workflows, focusing on automation, observability, and intelligent operations.

📌 Project Features

Order water cans (10L, 15L, 20L, 25L, 30L)

Simple WhatsApp-style message ordering

Automatic price calculation

REST API backend

Fully Dockerized application

Jenkins-based CI/CD pipeline

Designed for Kubernetes, Monitoring, and AIOps (next phases)

🧱 Tech Stack

Backend: Python (Flask)

Containerization: Docker

CI/CD: Jenkins

Source Control: GitHub

API Testing: Postman

Cloud (Planned): AWS EC2

Orchestration (Planned): Kubernetes

Monitoring (Planned): Prometheus & Grafana

AIOps: Ollama with Llama 3

🔁 Application Data Flow (DFD)

User (WhatsApp-style Order)
⬇
Postman / API Client
⬇
AquaFlow Flask REST API
⬇
Order Parsing & Billing Logic
⬇
JSON Response (Total Price)

🔄 CI/CD Workflow (DevOps Pipeline)

Developer (Vibhakar) pushes code
⬇
GitHub Repository
⬇
Jenkins Pipeline (Automated Trigger)
⬇
Docker Image Build
⬇
Docker Container Deployment

✔ Fully automated
✔ No manual deployment
✔ Production-style workflow

🐳 Containerization & Deployment

Flask application is packaged into a Docker image

Ensures:

Environment consistency

Easy deployment

Cloud & Kubernetes readiness

📊 Monitoring & Observability (Planned)

Prometheus collects metrics (CPU, memory, API latency)

Grafana visualizes system health dashboards

Enables proactive performance monitoring

🤖 AIOps – Critical Intelligence Layer (Llama 3)

AquaFlow integrates AIOps using Ollama with Llama 3 to add intelligence to DevOps operations.

How AIOps Helps This Project:

Intelligent Log Analysis
Analyzes application, Docker, and Jenkins logs

Anomaly Detection
Detects unusual failures and performance drops

Root Cause Insights
Identifies why builds, containers, or APIs fail

CI/CD Failure Intelligence
Explains Jenkins pipeline failures automatically

Predictive Operations (Future Scope)
Supports Kubernetes auto-scaling decisions

➡️ Transforms DevOps from reactive → proactive

📂 Project Structure
AquaFlow-Smart-Water-Delivery-Platform/
│
├── app/
│   └── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md
