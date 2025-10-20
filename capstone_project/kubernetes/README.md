# Plain Kubernetes Manifests for Manufacturing Copilot
# For users who prefer kubectl over Helm

This directory contains plain Kubernetes manifests that can be applied directly with `kubectl`.

## Quick Deploy

```bash
# Create namespace
kubectl create namespace manufacturing-copilot

# Create secret with HuggingFace token
kubectl create secret generic manufacturing-copilot \
  --from-literal=HUGGINGFACE_TOKEN=your_token_here \
  -n manufacturing-copilot

# Apply all manifests
kubectl apply -f kubernetes/ -n manufacturing-copilot

# Check deployment
kubectl get pods -n manufacturing-copilot
kubectl get svc -n manufacturing-copilot
```

## Files

- `namespace.yaml` - Namespace definition
- `configmap.yaml` - Application configuration
- `secret.yaml` - Sensitive data (template only)
- `serviceaccount.yaml` - Service account for pods
- `deployment.yaml` - Main application deployment
- `service.yaml` - ClusterIP service
- `ingress.yaml` - Ingress for external access
- `hpa.yaml` - Horizontal Pod Autoscaler
- `pdb.yaml` - Pod Disruption Budget
- `networkpolicy.yaml` - Network security policy
- `pvc.yaml` - Persistent volume claim for ChromaDB

## Customization

Edit the files to match your environment:
- Update image repository in `deployment.yaml`
- Update domain in `ingress.yaml`
- Update resource limits in `deployment.yaml`
- Set HuggingFace token in `secret.yaml` (or use kubectl create secret)
