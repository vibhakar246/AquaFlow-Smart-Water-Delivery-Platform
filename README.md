 🚰 AquaFlow – Smart Water Delivery Platform  
### DevOps CI/CD & AIOps Enabled Application  

**Author:** Vibhakar Kumar  

AquaFlow is a **smart water can delivery platform** built to demonstrate a **real-world DevOps CI/CD workflow**.  
The application processes **WhatsApp-style order messages**, performs **automatic billing**, supports a **payment-ready flow**, and follows **enterprise-grade DevOps practices with AIOps**.

---

## ✨ Key Features

- WhatsApp-style text-based ordering  
- Automatic billing & order summary  
- Payment-ready workflow (UPI / QR – extendable)  
- REST API built with Flask  
- Fully Dockerized application  
- Jenkins-based CI/CD automation  
- Designed for Kubernetes, Monitoring, and AIOps  

---

## 🧾 Order & Payment Flow

**Example Order Message**
2 x 20L, 1 x 10L


**System Actions**
- Parses order quantities and can sizes  
- Calculates total bill  
- Generates JSON response  

**Payment (Designed / Extendable)**
- Bill generated after order processing  
- Total amount returned to client  
- Ready for UPI / QR & payment callbacks  

---

## 🏗️ Application + DevOps Workflow

```mermaid
flowchart TD
    A[Developer<br/>GitHub Repo] --> B[Jenkins CI/CD Pipeline]

    B --> C[Build Docker Image]
    C --> D[Docker Container]

    D --> E[Flask REST API<br/>AquaFlow App]
    E --> F[Order Parsing and Billing Logic]
    F --> G[Payment Flow<br/>UPI / QR Ready]
    G --> H[JSON Response<br/>Order Summary]

    D --> I[Monitoring<br/>Prometheus and Grafana]
    D --> J[AIOps<br/>Llama 3 Log Analysis]





 CI/CD Pipeline
Code pushed to GitHub

Jenkins pipeline triggers automatically

Docker image built and deployed

Fully automated (no manual steps)

Containerization
Flask app packaged as a Docker image

Ensures:

Environment consistency

Easy deployment

Cloud & Kubernetes readiness

🤖 AIOps – Why It Matters (Llama 3)
Intelligent log analysis (App, Docker, Jenkins)

Anomaly detection & root-cause insights

CI/CD failure intelligence

Predictive operations (future Kubernetes scaling)

 Moves DevOps from reactive → proactive.

 Tech Stack
Backend: Python (Flask)

CI/CD: Jenkins

Containerization: Docker

Source Control: GitHub

API Testing: Postman

Monitoring: Prometheus & Grafana (planned)

AIOps: Ollama with Llama 3

Cloud / Orchestration: AWS EC2, Kubernetes (planned)

 Project Structure
AquaFlow-Smart-Water-Delivery-Platform/
├── app/
│   └── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md
