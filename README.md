# AquaFlow – Smart Water Delivery Platform 🚰

AquaFlow is a smart water can delivery application designed to demonstrate a **real-world DevOps CI/CD pipeline**.  
The platform processes simple WhatsApp-style order messages and calculates billing automatically.

This project focuses on **DevOps, CI/CD, containerization, monitoring, and AIOps**, following company-standard practices.

---

## 📌 Project Features

- Order water cans (10L, 15L, 20L, 25L, 30L)
- Simple message-based ordering
- Automatic price calculation
- REST API backend
- Dockerized application
- Jenkins-based CI/CD pipeline
- Designed for Kubernetes, Monitoring, and AIOps (next phases)

---

## 🧱 Tech Stack

- Backend: Python (Flask)
- Containerization: Docker
- CI/CD: Jenkins
- Source Control: GitHub
- API Testing: Postman
- Cloud (Planned): AWS EC2
- Orchestration (Planned): Kubernetes
- Monitoring (Planned): Prometheus & Grafana
- AIOps (Planned): Ollama with Llama 3

---

## 🔁 Data Flow Diagram (DFD)

# AquaFlow – Smart Water Delivery Platform 🚰

AquaFlow is a smart water can delivery application designed to demonstrate a **real-world DevOps CI/CD pipeline**.  
The platform processes simple WhatsApp-style order messages and calculates billing automatically.

This project focuses on **DevOps, CI/CD, containerization, monitoring, and AIOps**, following company-standard practices.

---

## 📌 Project Features

- Order water cans (10L, 15L, 20L, 25L, 30L)
- Simple message-based ordering
- Automatic price calculation
- REST API backend
- Dockerized application
- Jenkins-based CI/CD pipeline
- Designed for Kubernetes, Monitoring, and AIOps (next phases)

---

## 🧱 Tech Stack

- Backend: Python (Flask)
- Containerization: Docker
- CI/CD: Jenkins
- Source Control: GitHub
- API Testing: Postman
- Cloud (Planned): AWS EC2
- Orchestration (Planned): Kubernetes
- Monitoring (Planned): Prometheus & Grafana
- AIOps (Planned): Ollama with Llama 3

---

## 🔁 Data Flow Diagram (DFD)

User (WhatsApp-style Order)
|
v
Postman / API Client
|
v
AquaFlow Flask API
|
v
Order Parsing & Billing Logic
|
v
JSON Response (Total Price)


---

## 🔄 CI/CD Flow



Developer Pushes Code
|
v
GitHub Repository
|
v
Jenkins Pipeline
|
v
Docker Image Build
|
v
Docker Container Deployment


---

## 📂 Project Structure



AquaFlow-Smart-Water-Delivery-Platform/
│
├── app/
│ └── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md



