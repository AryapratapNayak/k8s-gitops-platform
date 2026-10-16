# Kubernetes GitOps Platform

A Kubernetes microservices platform using Helm, Argo CD, and Prometheus-Grafana monitoring.

## Services
- Frontend
- Backend
- User Service

## Technology Stack
- Kubernetes (kind)
- Docker
- Helm
- Argo CD
- Prometheus
- Grafana
- Alertmanager

## Verified Status
- Argo CD applications were verified Synced and Healthy.
- Monitoring components were verified Running and Ready.
- Grafana dashboards were configured.
- Slack alert configuration was applied; message delivery is not yet verified.
- Local ingress access was previously tested successfully.
- AWS EKS deployment has not been verified.

## Useful Commands

Check Argo CD applications:

    kubectl get applications -n argocd

Check pods:

    kubectl get pods -n staging

    kubectl get pods -n monitoring

Check autoscaling:

    kubectl get hpa -n staging

Open Grafana locally:

    kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80

Then open http://localhost:3000.
