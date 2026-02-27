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

```mermaid

flowchart TD
    A[Receive Order Message] --> B[Regex Parsing]
    B --> C{Valid Items?}
    C -- No --> D[Return 400 Error]
    C -- Yes --> E[Calculate Subtotal]
    E --> F[Apply 18% GST]
    F --> G{Subtotal < 200?}
    G -- Yes --> H[Add 20 Delivery]
    G -- No --> I[Free Delivery]
    H --> J[Generate Final Bill]
    I --> J
    J --> K[Return JSON Response]

```mermaid
flowchart TD
    A[API Endpoints]
    A --> B[GET /]
    A --> C[GET /api/health]
    A --> D[POST /api/order]

```mermaid

flowchart TD
    A[Monitoring Tool] -->|GET /api/health| B[Flask Server]
    B --> C[Check Service Status]
    C --> D[Return JSON Status + Timestamp]





