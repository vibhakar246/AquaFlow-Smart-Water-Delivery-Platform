# AquaFlow – Smart Water Delivery Platform 🚰

## 📌 Overview
AquaFlow is a production-ready smart water delivery platform that enables WhatsApp-style text-based order placement, automatic bill calculation with GST, and containerized deployment with a complete DevOps CI/CD workflow.

This project demonstrates **backend development + DevOps practices**, including API development, testing, Dockerization, CI/CD pipelines, health checks, and cloud deployment readiness.

---

## ✨ Features
- 📱 WhatsApp-style text order parsing
- 🧾 Automatic bill calculation with GST
- ❤️ Health check API for service monitoring
- 🧪 Unit & integration testing
- 🐳 Dockerized application
- 🔁 Jenkins CI/CD pipeline
- ☁️ Cloud-ready deployment (AWS EC2)

---

## 🏗️ Tech Stack

**Backend**
- Python
- Flask

**Testing**
- PyTest (unit & integration tests)

**CI/CD**
- Jenkins

**Containerization**
- Docker

**Cloud**
- AWS EC2

  ---
### Health Check API

The application exposes a health check API used to verify service availability and readiness.

- Endpoint: `/api/health`
- Method: `GET`
- Response: Service name, health status, and timestamp
- Used for application monitoring and Docker container health validation


<img width="1920" height="1080" alt="helthc" src="https://github.com/user-attachments/assets/bb00b768-a5e4-46db-92a2-4e90a8b5ea41" />

- AWS EC2

---
