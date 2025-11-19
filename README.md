Task Runner Microservice (K8s Exercise)

This repo contains a small FastAPI microservice + Kubernetes manifests for:

- Deployment with probes and resource limits
- Service (ClusterIP)
- Horizontal Pod Autoscaler
- Kubernetes Job (one time workflow)
- CronJob (scheduled workflow)
- CI pipeline (lint and Docker build)
  
Summary:
run_task() is a small fake workload generator that pretends to run a job by sleeping for 2 – 5 seconds and returning a unique task ID.
