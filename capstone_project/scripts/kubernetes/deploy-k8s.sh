#!/bin/bash
# Kubernetes Deployment Script for Manufacturing Copilot
# Usage: ./deploy-k8s.sh [dev|prod]

set -e

# Configuration
NAMESPACE="manufacturing-copilot"
ENVIRONMENT=${1:-dev}
KUBECONFIG=${KUBECONFIG:-~/.kube/config}

echo "🚀 Deploying Manufacturing Copilot to Kubernetes"
echo "Environment: $ENVIRONMENT"
echo "Namespace: $NAMESPACE"
echo ""

# Check prerequisites
echo "📋 Checking prerequisites..."
command -v kubectl >/dev/null 2>&1 || { echo "❌ kubectl not found. Please install kubectl."; exit 1; }
command -v helm >/dev/null 2>&1 || { echo "⚠️  helm not found. Using kubectl instead."; HELM_AVAILABLE=false; }

# Check cluster connection
kubectl cluster-info >/dev/null 2>&1 || { echo "❌ Cannot connect to Kubernetes cluster. Check your kubeconfig."; exit 1; }
echo "✅ Connected to cluster: $(kubectl config current-context)"

# Prompt for HuggingFace token
if [ -z "$HUGGINGFACE_TOKEN" ]; then
    echo ""
    echo "🔑 HuggingFace API Token Required"
    read -sp "Enter your HuggingFace token (will be hidden): " HUGGINGFACE_TOKEN
    echo ""
    if [ -z "$HUGGINGFACE_TOKEN" ]; then
        echo "❌ HuggingFace token is required"
        exit 1
    fi
fi

# Create namespace if it doesn't exist
echo ""
echo "📦 Creating namespace..."
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

# Deploy using Helm if available
if [ "$HELM_AVAILABLE" != "false" ]; then
    echo ""
    echo "🎯 Deploying with Helm..."
    
    # Add Helm chart dependencies (if any)
    helm dependency update charts/manufacturing-copilot/ || true
    
    # Deploy with environment-specific values
    helm upgrade --install manufacturing-copilot \
        ./charts/manufacturing-copilot \
        --namespace $NAMESPACE \
        --values ./charts/manufacturing-copilot/values-$ENVIRONMENT.yaml \
        --set secrets.huggingfaceToken="$HUGGINGFACE_TOKEN" \
        --create-namespace \
        --wait \
        --timeout 10m
    
    echo "✅ Helm deployment complete!"
else
    # Deploy with kubectl
    echo ""
    echo "🎯 Deploying with kubectl..."
    
    # Create secret
    kubectl create secret generic manufacturing-copilot-secret \
        --from-literal=HUGGINGFACE_TOKEN="$HUGGINGFACE_TOKEN" \
        --namespace=$NAMESPACE \
        --dry-run=client -o yaml | kubectl apply -f -
    
    # Apply manifests
    kubectl apply -f kubernetes/ --namespace=$NAMESPACE
    
    echo "✅ kubectl deployment complete!"
fi

# Wait for deployment
echo ""
echo "⏳ Waiting for pods to be ready..."
kubectl wait --for=condition=ready pod \
    --selector=app=manufacturing-copilot \
    --namespace=$NAMESPACE \
    --timeout=5m || {
    echo "⚠️  Pods not ready yet. Check status with:"
    echo "   kubectl get pods -n $NAMESPACE"
    echo "   kubectl logs -n $NAMESPACE -l app=manufacturing-copilot"
}

# Display deployment status
echo ""
echo "📊 Deployment Status:"
echo "===================="
kubectl get deployments -n $NAMESPACE
echo ""
kubectl get pods -n $NAMESPACE
echo ""
kubectl get svc -n $NAMESPACE

# Display access information
echo ""
echo "🌐 Access Information:"
echo "====================="

# Check if ingress is enabled
INGRESS_HOST=$(kubectl get ingress -n $NAMESPACE -o jsonpath='{.items[0].spec.rules[0].host}' 2>/dev/null || echo "")
if [ -n "$INGRESS_HOST" ]; then
    echo "Ingress URL: https://$INGRESS_HOST"
else
    echo "No ingress configured. Use port-forward to access:"
    echo "  kubectl port-forward svc/manufacturing-copilot 8080:8080 -n $NAMESPACE"
    echo "  Then access: http://localhost:8080"
fi

echo ""
echo "✨ Deployment successful!"
echo ""
echo "📚 Next steps:"
echo "  - View logs: kubectl logs -n $NAMESPACE -l app=manufacturing-copilot --tail=100"
echo "  - Scale pods: kubectl scale deployment manufacturing-copilot --replicas=3 -n $NAMESPACE"
echo "  - Update config: kubectl edit configmap manufacturing-copilot-config -n $NAMESPACE"
echo "  - Delete: helm uninstall manufacturing-copilot -n $NAMESPACE (or kubectl delete namespace $NAMESPACE)"
