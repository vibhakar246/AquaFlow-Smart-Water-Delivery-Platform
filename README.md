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
### Health Check API & Integration Testing

This screenshot demonstrates both the Health Check API and the execution of integration tests.

- Health Check API (`/api/health`) confirms the application is running and healthy
- Integration tests validate order processing and bill calculation
- Error scenarios such as invalid and empty orders are handled correctly
- All tests complete successfully, indicating application stability


<img width="1920" height="1080" alt="helthc" src="https://github.com/user-attachments/assets/bb00b768-a5e4-46db-92a2-4e90a8b5ea41" />

### Dockerfile (Production-Ready Containerization)

This screenshot shows the Dockerfile used to containerize the AquaFlow application.

- Uses a lightweight Python base image
- Installs dependencies in a clean and efficient way
- Runs the application as a non-root user for security
- Includes a container-level health check
- Uses Gunicorn as the production WSGI server
<img width="1920" height="1080" alt="Screenshot 2026-02-03 135919" src="https://github.com/user-attachments/assets/e1b8fbb9-27eb-491a-bcdd-35e8858ade4e" />



