# 🚰 AquaFlow – Smart Water Delivery Platform  
### DevOps CI/CD & AIOps Enabled Application  

**Author:** Vibhakar Kumar  

AquaFlow is a **smart water can delivery platform** built to demonstrate a **real-world DevOps CI/CD workflow**.  
The application processes **WhatsApp-style order messages**, generates **automatic billing**, supports a **payment-ready flow**, and implements **modern DevOps practices with AIOps**.

This project follows **enterprise-grade DevOps standards**, focusing on **automation, observability, scalability, and intelligent operations**.

---

## ✨ Key Features

- WhatsApp-style text-based ordering  
- Automatic billing & order summary  
- Payment-ready workflow (UPI / QR – extendable)  
- REST API built using Flask  
- Fully Dockerized application  
- Jenkins-based CI/CD automation  
- Designed for Kubernetes, Monitoring, and AIOps  

---

## 🧾 WhatsApp-Style Order Format

**Example Order Message**
2 x 20L, 1 x 10L

**System Actions**
- Parses order quantities and can sizes  
- Calculates total bill  
- Generates structured JSON response  

---

## 💳 Payment Flow (Designed / Extendable)

- Bill generated after order processing  
- Returns total payable amount  
- Ready for integration with:
  - UPI / QR code payments
  - Payment confirmation callbacks  

---
## 🏗️ System Architecture & Workflow

```mermaid
sequenceDiagram
    autonumber

    participant U as User (WhatsApp Order)
    participant C as API Client
    participant API as Flask API
    participant BL as Billing Logic
    participant PAY as Payment System
    participant G as GitHub
    participant J as Jenkins
    participant D as Docker
    participant APP as Running Application
    participant M as Monitoring (Prometheus/Grafana)
    participant AI as AIOps (Llama 3)

    %% Order & Billing Flow
    U->>C: Place order message
    C->>API: Send order request
    API->>BL: Parse order & calculate bill
    BL-->>API: Bill details
    API-->>C: Order summary

    %% Payment Flow
    C->>PAY: Initiate payment (UPI / QR)
    PAY-->>C: Payment confirmation
    C->>API: Send payment status
    API-->>C: Final response

    %% CI/CD Flow
    U->>G: Push code
    G->>J: Trigger CI/CD pipeline
    J->>D: Build Docker image
    D->>APP: Deploy container

    %% Monitoring & AIOps
    APP->>M: Expose metrics
    APP->>AI: Send logs
    AI-->>M: Anomaly detection & insights


🔄 CI/CD Pipeline

Code pushed to GitHub

Jenkins pipeline triggers automatically

Application is built and packaged as a Docker image

Container is deployed

✔ Fully automated
✔ No manual deployment

🐳 Containerization

Flask application packaged as a Docker image

Ensures:

Environment consistency

Easy deployment

Cloud & Kubernetes readiness

📊 Monitoring & Observability (Planned)

Prometheus collects metrics (CPU, memory, API latency)

Grafana visualizes system health dashboards

Enables proactive performance monitoring

🤖 AIOps – Why It Matters (Llama 3)

AquaFlow integrates AIOps using Ollama with Llama 3.

AIOps Capabilities

Intelligent log analysis (App, Docker, Jenkins logs)

Anomaly detection & root-cause insights

CI/CD failure intelligence

Predictive operations (future Kubernetes auto-scaling)

➡️ Transforms DevOps from reactive → proactive.

🧱 Tech Stack

Backend: Python (Flask)

CI/CD: Jenkins

Containerization: Docker

Source Control: GitHub

API Testing: Postman

Monitoring: Prometheus & Grafana (planned)

AIOps: Ollama with Llama 3

Cloud / Orchestration: AWS EC2, Kubernetes (planned)

📂 Project Structure
AquaFlow-Smart-Water-Delivery-Platform/
├── app/
│   └── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md
