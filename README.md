# 🚰 AquaFlow – DevOps-Ready Water Delivery API

AquaFlow is a Flask-based REST API designed to process water delivery orders from text input, calculate billing with tax and delivery logic, and return structured JSON responses.

The application is built with clean business logic and DevOps-ready architecture.

---

## 🏗 System Architecture

```mermaid
flowchart LR
    A[Client / User] -->|HTTP Request| B[Flask API Server]
    B --> C[Order Parsing Engine]
    C --> D[Product Catalog]
    C --> E[Billing Calculator]
    E --> F[Tax & Delivery Logic]
    B -->|JSON Response| A

flowchart TD
    A[Receive Order Message] --> B[Regex Parsing]
    B --> C{Valid Items?}
    C -- No --> D[Return 400 Error]
    C -- Yes --> E[Calculate Subtotal]
    E --> F[Apply 18% GST]
    F --> G{Subtotal < 200?}
    G -- Yes --> H[Add ₹20 Delivery]
    G -- No --> I[Free Delivery]
    H --> J[Generate Final Bill]
    I --> J
    J --> K[Return JSON Response]
flowchart TD
    A[API Endpoints]
    A --> B[GET /]
    A --> C[GET /api/health]
    A --> D[POST /api/order]

flowchart LR
    A[Developer Push Code] --> B[GitHub Repository]
    B --> C[CI/CD Pipeline]
    C --> D[Docker Build]
    D --> E[Docker Image]
    E --> F[Container Runtime]
    F --> G[AquaFlow API Running]


flowchart TD
    A[Monitoring Tool] -->|GET /api/health| B[Flask Server]
    B --> C[Check Service Status]
    C --> D[Return JSON Status + Timestamp]


flowchart LR
    A[Python 3] --> B[Flask]
    B --> C[REST API]
    C --> D[JSON]
    D --> E[Docker Ready]
    E --> F[CI/CD Compatible]

flowchart TD
    A[DevOps Implementation]
    A --> B[Containerization - Docker]
    A --> C[CI/CD Pipeline Integration]
    A --> D[Health Monitoring Endpoint]
    A --> E[Production Deployment Ready]
    A --> F[Cloud Deployment Compatible]
👨‍💻 Author

Vibhakar Kumar

