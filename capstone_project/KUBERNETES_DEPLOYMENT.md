# 🚢 Kubernetes Deployment Guide - Manufacturing Copilot

> **Complete guide to deploying Manufacturing Copilot on Kubernetes clusters (GKE, EKS, AKS, or self-managed)**

## 📋 Table of Contents

- [Prerequisites](#-prerequisites)
- [Quick Deploy](#-quick-deploy-5-minutes)
- [Deployment Options](#-deployment-options)
- [Cloud-Specific Guides](#-cloud-specific-guides)
- [Configuration](#-configuration)
- [Monitoring & Scaling](#-monitoring--scaling)
- [Troubleshooting](#-troubleshooting)
- [Production Checklist](#-production-checklist)

---

## ✅ Prerequisites

### Required Tools

- **kubectl** 1.24+ ([install](https://kubernetes.io/docs/tasks/tools/))
- **Helm** 3.0+ (optional but recommended) ([install](https://helm.sh/docs/intro/install/))
- **Docker** (for building custom images) ([install](https://docs.docker.com/get-docker/))
- **HuggingFace API Token** ([get token](https://huggingface.co/settings/tokens))

### Kubernetes Cluster

You need access to a Kubernetes cluster. Options:

- **Google Kubernetes Engine (GKE)** - Recommended for beginners
- **Amazon EKS** - AWS users
- **Azure AKS** - Azure users
- **Minikube** - Local development
- **Kind** - Local testing
- **Self-managed** - On-premise or custom cloud

### Cluster Requirements

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| **Nodes** | 2 | 3+ |
| **CPU per node** | 2 cores | 4 cores |
| **Memory per node** | 4 GB | 8 GB |
| **Storage** | 20 GB | 50 GB |
| **Kubernetes version** | 1.24+ | 1.28+ |

---

## 🚀 Quick Deploy (5 Minutes)

### Option 1: Using Helm (Recommended)

```bash
# 1. Clone repository
git clone https://github.com/abhayra12/Gen-AI-Roadmap.git
cd Gen-AI-Roadmap/capstone_project

# 2. Run deployment script
chmod +x scripts/kubernetes/deploy-k8s.sh
./scripts/kubernetes/deploy-k8s.sh dev

# Or Windows PowerShell:
.\scripts\kubernetes\deploy-k8s.ps1 -Environment dev

# 3. Access the API
kubectl port-forward svc/manufacturing-copilot 8080:8080 -n manufacturing-copilot
# Open http://localhost:8080/docs
```

### Option 2: Using kubectl Only

```bash
# 1. Create namespace
kubectl create namespace manufacturing-copilot

# 2. Create secret with your HuggingFace token
kubectl create secret generic manufacturing-copilot-secret \
  --from-literal=HUGGINGFACE_TOKEN=hf_your_token_here \
  --namespace=manufacturing-copilot

# 3. Apply manifests
kubectl apply -f kubernetes/ --namespace=manufacturing-copilot

# 4. Wait for pods
kubectl wait --for=condition=ready pod \
  --selector=app=manufacturing-copilot \
  --namespace=manufacturing-copilot \
  --timeout=5m

# 5. Check status
kubectl get pods -n manufacturing-copilot
```

---

## 📦 Deployment Options

### 1. Helm Chart Deployment (Production-Ready)

**Why Helm?**
- ✅ Easy configuration management
- ✅ Environment-specific values (dev/prod)
- ✅ Version control and rollbacks
- ✅ Dependency management

**Deploy with Helm:**

```bash
# Development
helm install copilot ./charts/manufacturing-copilot \
  --namespace manufacturing-copilot \
  --create-namespace \
  --values ./charts/manufacturing-copilot/values-dev.yaml \
  --set secrets.huggingfaceToken="hf_your_token_here"

# Production
helm install copilot ./charts/manufacturing-copilot \
  --namespace manufacturing-copilot \
  --create-namespace \
  --values ./charts/manufacturing-copilot/values-prod.yaml \
  --set secrets.huggingfaceToken="hf_your_token_here" \
  --set image.tag="v1.0.0"

# Upgrade
helm upgrade copilot ./charts/manufacturing-copilot \
  --namespace manufacturing-copilot \
  --values ./charts/manufacturing-copilot/values-prod.yaml \
  --reuse-values

# Rollback
helm rollback copilot 1 --namespace manufacturing-copilot

# Uninstall
helm uninstall copilot --namespace manufacturing-copilot
```

### 2. Plain Kubernetes Manifests

**Use this if:**
- You don't have Helm
- You prefer GitOps workflows (ArgoCD, Flux)
- You want full control over manifests

```bash
# Apply all manifests
kubectl apply -f kubernetes/ --namespace=manufacturing-copilot

# Apply selectively
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/configmap.yaml
kubectl apply -f kubernetes/secret.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/ingress.yaml
kubectl apply -f kubernetes/hpa.yaml
kubectl apply -f kubernetes/pdb.yaml
```

### 3. Kustomize Deployment

Create `kustomization.yaml`:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: manufacturing-copilot

resources:
  - kubernetes/namespace.yaml
  - kubernetes/configmap.yaml
  - kubernetes/secret.yaml
  - kubernetes/serviceaccount.yaml
  - kubernetes/pvc.yaml
  - kubernetes/deployment.yaml
  - kubernetes/service.yaml
  - kubernetes/ingress.yaml
  - kubernetes/hpa.yaml
  - kubernetes/pdb.yaml
  - kubernetes/networkpolicy.yaml

secretGenerator:
  - name: manufacturing-copilot-secret
    literals:
      - HUGGINGFACE_TOKEN=hf_your_token_here

images:
  - name: abhayra12/manufacturing-copilot
    newTag: v1.0.0
```

**Deploy:**

```bash
kubectl apply -k .
```

---

## ☁️ Cloud-Specific Guides

### Google Kubernetes Engine (GKE)

**1. Create GKE Cluster:**

```bash
# Set variables
export PROJECT_ID=your-gcp-project
export CLUSTER_NAME=manufacturing-copilot-cluster
export REGION=us-central1

# Enable APIs
gcloud services enable container.googleapis.com

# Create cluster
gcloud container clusters create $CLUSTER_NAME \
  --region=$REGION \
  --num-nodes=2 \
  --machine-type=e2-standard-4 \
  --enable-autoscaling \
  --min-nodes=2 \
  --max-nodes=10 \
  --enable-autorepair \
  --enable-autoupgrade \
  --project=$PROJECT_ID

# Get credentials
gcloud container clusters get-credentials $CLUSTER_NAME \
  --region=$REGION \
  --project=$PROJECT_ID
```

**2. Deploy with GKE-specific values:**

Update `values-prod.yaml`:

```yaml
ingress:
  className: "gce"
  annotations:
    kubernetes.io/ingress.class: "gce"
    kubernetes.io/ingress.global-static-ip-name: "copilot-ip"

persistence:
  storageClass: "pd-ssd"  # GKE SSD

serviceAccount:
  annotations:
    iam.gke.io/gcp-service-account: copilot-sa@your-project.iam.gserviceaccount.com
```

**3. Deploy:**

```bash
helm install copilot ./charts/manufacturing-copilot \
  --namespace manufacturing-copilot \
  --create-namespace \
  --values ./charts/manufacturing-copilot/values-prod.yaml \
  --set secrets.huggingfaceToken="$HUGGINGFACE_TOKEN"
```

---

### Amazon EKS

**1. Create EKS Cluster:**

```bash
# Install eksctl
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin

# Create cluster
eksctl create cluster \
  --name manufacturing-copilot-cluster \
  --region us-east-1 \
  --nodes 2 \
  --node-type t3.large \
  --managed

# Get credentials (automatic with eksctl)
```

**2. Install AWS Load Balancer Controller:**

```bash
# Add EKS repository
helm repo add eks https://aws.github.io/eks-charts
helm repo update

# Install AWS Load Balancer Controller
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  --namespace kube-system \
  --set clusterName=manufacturing-copilot-cluster \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller
```

**3. Deploy with EKS-specific values:**

Update `values-prod.yaml`:

```yaml
ingress:
  className: "alb"
  annotations:
    kubernetes.io/ingress.class: "alb"
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip

persistence:
  storageClass: "gp3"  # EKS GP3 SSD
```

---

### Azure AKS

**1. Create AKS Cluster:**

```bash
# Set variables
export RESOURCE_GROUP=manufacturing-copilot-rg
export CLUSTER_NAME=manufacturing-copilot-cluster
export LOCATION=eastus

# Create resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create cluster
az aks create \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME \
  --node-count 2 \
  --node-vm-size Standard_D4s_v3 \
  --enable-managed-identity \
  --enable-cluster-autoscaler \
  --min-count 2 \
  --max-count 10 \
  --generate-ssh-keys

# Get credentials
az aks get-credentials --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME
```

**2. Deploy with AKS-specific values:**

Update `values-prod.yaml`:

```yaml
persistence:
  storageClass: "managed-premium"  # AKS Premium SSD
```

---

### Minikube (Local Development)

```bash
# Start minikube
minikube start --cpus=4 --memory=8192

# Enable ingress addon
minikube addons enable ingress

# Deploy
helm install copilot ./charts/manufacturing-copilot \
  --namespace manufacturing-copilot \
  --create-namespace \
  --values ./charts/manufacturing-copilot/values-dev.yaml \
  --set secrets.huggingfaceToken="$HUGGINGFACE_TOKEN"

# Access via minikube tunnel
minikube tunnel

# Or port-forward
kubectl port-forward svc/manufacturing-copilot 8080:8080 -n manufacturing-copilot
```

---

## ⚙️ Configuration

### Environment Variables

Configured via `ConfigMap` and `Secret`:

**ConfigMap (kubernetes/configmap.yaml):**

```yaml
data:
  APP_TITLE: "Manufacturing Copilot API"
  LOG_LEVEL: "INFO"
  VLM_MODEL_ID: "Salesforce/blip2-opt-2.7b"
  LLM_MODEL_ID: "meta-llama/Llama-2-7b-chat-hf"
  # ... more config
```

**Update config:**

```bash
kubectl edit configmap manufacturing-copilot-config -n manufacturing-copilot
# Restart pods to apply:
kubectl rollout restart deployment manufacturing-copilot -n manufacturing-copilot
```

### Secrets Management

**Option 1: kubectl (Simple)**

```bash
kubectl create secret generic manufacturing-copilot-secret \
  --from-literal=HUGGINGFACE_TOKEN=hf_your_token_here \
  --namespace=manufacturing-copilot
```

**Option 2: Sealed Secrets (GitOps-friendly)**

```bash
# Install Sealed Secrets controller
helm install sealed-secrets sealed-secrets/sealed-secrets \
  --namespace kube-system

# Create sealed secret
echo -n hf_your_token_here | kubectl create secret generic manufacturing-copilot-secret \
  --dry-run=client \
  --from-file=HUGGINGFACE_TOKEN=/dev/stdin \
  -o yaml | \
  kubeseal -o yaml > sealed-secret.yaml

# Apply sealed secret (safe to commit to Git)
kubectl apply -f sealed-secret.yaml
```

**Option 3: External Secrets Operator**

```bash
# Install External Secrets Operator
helm install external-secrets \
  external-secrets/external-secrets \
  --namespace external-secrets-system \
  --create-namespace

# Create SecretStore (example for AWS Secrets Manager)
kubectl apply -f - <<EOF
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secrets-manager
  namespace: manufacturing-copilot
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-east-1
---
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: manufacturing-copilot-secret
  namespace: manufacturing-copilot
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: SecretStore
  target:
    name: manufacturing-copilot-secret
  data:
  - secretKey: HUGGINGFACE_TOKEN
    remoteRef:
      key: manufacturing-copilot/huggingface-token
EOF
```

---

## 📊 Monitoring & Scaling

### Horizontal Pod Autoscaling

**Already configured in `kubernetes/hpa.yaml`:**

```bash
# Check HPA status
kubectl get hpa -n manufacturing-copilot

# Manually scale
kubectl scale deployment manufacturing-copilot --replicas=5 -n manufacturing-copilot
```

### Monitoring with Prometheus

**Install Prometheus Operator:**

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace
```

**ServiceMonitor is already configured** in Helm chart when monitoring is enabled.

### Logging

**View logs:**

```bash
# All pods
kubectl logs -n manufacturing-copilot -l app=manufacturing-copilot --tail=100

# Follow logs
kubectl logs -n manufacturing-copilot -l app=manufacturing-copilot -f

# Specific pod
kubectl logs -n manufacturing-copilot manufacturing-copilot-xxxx-yyyy
```

**Centralized logging with Fluentd:**

```bash
helm install fluentd fluent/fluentd \
  --namespace logging \
  --create-namespace
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Pods stuck in "Pending"

**Check:**

```bash
kubectl describe pod manufacturing-copilot-xxx -n manufacturing-copilot
```

**Solutions:**
- **Insufficient resources:** Scale up cluster or reduce resource requests
- **PVC not bound:** Check storage class exists
  ```bash
  kubectl get sc
  kubectl get pvc -n manufacturing-copilot
  ```

#### 2. Pods crash looping

**Check logs:**

```bash
kubectl logs manufacturing-copilot-xxx -n manufacturing-copilot --previous
```

**Common causes:**
- Missing HUGGINGFACE_TOKEN
- Invalid configuration
- Out of memory (increase limits in values.yaml)

#### 3. Cannot access service

**Check service:**

```bash
kubectl get svc -n manufacturing-copilot
kubectl describe svc manufacturing-copilot -n manufacturing-copilot
```

**Port-forward to test:**

```bash
kubectl port-forward svc/manufacturing-copilot 8080:8080 -n manufacturing-copilot
curl http://localhost:8080/health
```

#### 4. Ingress not working

**Check ingress:**

```bash
kubectl get ingress -n manufacturing-copilot
kubectl describe ingress manufacturing-copilot -n manufacturing-copilot
```

**Verify ingress controller is installed:**

```bash
kubectl get pods -n ingress-nginx  # For NGINX
kubectl get pods -n kube-system | grep ingress  # For GKE/cloud providers
```

### Debug Commands

```bash
# Get pod details
kubectl describe pod <pod-name> -n manufacturing-copilot

# Get events
kubectl get events -n manufacturing-copilot --sort-by='.lastTimestamp'

# Execute command in pod
kubectl exec -it <pod-name> -n manufacturing-copilot -- /bin/sh

# Check resource usage
kubectl top pods -n manufacturing-copilot
kubectl top nodes

# Validate manifests
kubectl apply --dry-run=client -f kubernetes/

# Check RBAC permissions
kubectl auth can-i create deployments --namespace=manufacturing-copilot
```

---

## ✅ Production Checklist

### Security

- [ ] **Secrets management**: Use external secrets operator or sealed secrets
- [ ] **Network policies**: Enabled and tested
- [ ] **Pod security**: SecurityContext configured (non-root, read-only FS)
- [ ] **RBAC**: Least privilege service account
- [ ] **TLS/SSL**: Ingress with valid certificates
- [ ] **Image scanning**: Scan images for vulnerabilities
- [ ] **Private registry**: Use private container registry

### Reliability

- [ ] **Resource limits**: CPU and memory limits set
- [ ] **Health checks**: Liveness, readiness, startup probes configured
- [ ] **Pod Disruption Budget**: Configured to maintain availability
- [ ] **Horizontal Pod Autoscaler**: Enabled and tested
- [ ] **Multi-zone**: Pods spread across availability zones
- [ ] **Backup**: ChromaDB data backed up regularly

### Monitoring

- [ ] **Metrics**: Prometheus ServiceMonitor configured
- [ ] **Logging**: Centralized logging setup
- [ ] **Alerting**: Alerts for pod failures, high resource usage
- [ ] **Dashboards**: Grafana dashboards created
- [ ] **Tracing**: Distributed tracing (optional)

### Performance

- [ ] **Resource requests**: Appropriate requests for consistent scheduling
- [ ] **Node affinity**: Pods scheduled on appropriate nodes
- [ ] **Storage class**: SSD storage for ChromaDB
- [ ] **Caching**: Review caching strategy for LLM responses
- [ ] **Load testing**: Tested with expected traffic

### Operations

- [ ] **CI/CD**: Automated deployments configured
- [ ] **GitOps**: ArgoCD or Flux CD setup (optional)
- [ ] **Rollback strategy**: Tested rollback procedures
- [ ] **Documentation**: Runbooks for common operations
- [ ] **Disaster recovery**: Recovery plan documented and tested

---

## 📚 Additional Resources

- **Kubernetes Docs**: https://kubernetes.io/docs/
- **Helm Docs**: https://helm.sh/docs/
- **GKE Guide**: https://cloud.google.com/kubernetes-engine/docs
- **EKS Guide**: https://docs.aws.amazon.com/eks/
- **AKS Guide**: https://docs.microsoft.com/en-us/azure/aks/
- **Minikube**: https://minikube.sigs.k8s.io/docs/

---

**Questions? See main [README.md](README.md) or [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)**

**Built with ❤️ for production Kubernetes deployments** 🚀
