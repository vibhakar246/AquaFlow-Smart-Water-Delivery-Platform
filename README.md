## 🏗️ DevOps Architecture Diagram

```mermaid
flowchart TD

    subgraph Frontend
        A[Customer Request]
    end

    subgraph DevOps Infrastructure
        B[GitHub Repository]
        C[Jenkins CI/CD]
        D[Ansible Deployment]
        E[Argo CD GitOps]
        F[Docker Container<br/>Python 3.9 Slim]

        B --> C
        C --> D
        D --> E
        C --> F
        E --> F
    end

    subgraph Flask Application
        G[API Gateway]
        H[Regex Order Parser]
        I[Bill Calculator<br/>GST: 18%]
        J[Product Catalog<br/>20L | 10L | 5L | 1L]

        G --> H
        H --> I
        I --> J
    end

    A --> G
    F --> G
```
