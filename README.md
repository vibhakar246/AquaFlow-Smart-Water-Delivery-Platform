🚰 AquaFlow Water Delivery API
Clean Water Delivery, Powered by Modern DevOps

A production-ready Flask REST API that processes natural text water orders, calculates GST + delivery charges, and is fully containerized with CI/CD and GitOps deployment support.
graph TB
    subgraph "Frontend"
        C[Customer Request]
    end
    
    subgraph "Flask Application (Port 5001)"
        A[API Gateway]
        B[Regex Order Parser]
        D[Bill Calculator<br/>GST: 18%]
        E[Product Catalog<br/>20L | 10L | 5L | 1L]
    end
    
    subgraph "DevOps Infrastructure"
        F[Docker Container<br/>Python 3.9 Slim]
        G[Jenkins CI/CD]
        H[Ansible Deployment]
        I[Argo CD GitOps]
        J[GitHub Repository]
    end
    
    C --> A
    A --> B
    B --> D
    D --> E
    
    J --> G
    G --> F
    G --> H
    H --> I
    I --> F
    F --> A
    flowchart LR
    A[GET /] --> B["Home Response"]
    C[GET /api/health] --> D["Service Status + Timestamp"]
    E[POST /api/order] --> F["Parse Order + Calculate Bill"]
flowchart TD
    A[Calculate Subtotal]
    --> B[Apply 18% GST]
    --> C{Subtotal < ₹200?}
    C -- Yes --> D[Add ₹20 Delivery]
    C -- No --> E[Free Delivery]
    D --> F[Final Total]
    E --> F
    
   graph LR
    A[Git Push] --> B[Checkout Code]
    B --> C[Run Tests]
    C --> D[Build Docker Image]
    D --> E[Push to Registry]
    E --> F[Deploy via Ansible] 
    
