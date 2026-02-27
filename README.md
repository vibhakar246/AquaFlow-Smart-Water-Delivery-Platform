### Integration Tests

- Integration tests validate order processing and bill calculation.
- Error scenarios such as invalid and empty orders are handled correctly.
- All tests complete successfully, indicating application stability.

graph TD
    subgraph "Test Suite"
        T1[Valid Order Test<br/>2x20L, 3x10L] --> P[✅ PASS]
        T2[Invalid Order Test<br/>Invalid Format] --> P
        T3[Empty Order Test<br/>No Message] --> P
        T4[Delivery Logic Test<br/>Subtotal < ₹200] --> P
    end



---

### Dockerfile (Production-Ready Containerization)

This Dockerfile containerizes the AquaFlow application in a production-ready environment:

- Uses a lightweight Python base image
- Installs dependencies efficiently
- Runs application as a non-root user for security
- Includes container health checks
- Uses Gunicorn as the production WSGI server

---

### DevOps Skills Demonstrated

- Docker containerization
- CI/CD pipeline automation (Jenkins)
- Infrastructure automation (Ansible)
- GitOps deployment concepts (Argo CD)

mindmap
  root((DevOps<br/>Capabilities))
    Containerization
      Docker
      Multi-stage builds
      Health checks
      Non-root user
    CI/CD
      Jenkins
      Pipeline as Code
      Automated Testing
      Build & Deploy
    Configuration Mgmt
      Ansible
      Playbooks
      Idempotency
    GitOps
      Argo CD
      Declarative Config
      Auto-sync
      Rollback




