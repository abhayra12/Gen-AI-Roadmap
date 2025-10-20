# PowerShell Deployment Script for Kubernetes
# Usage: .\deploy-k8s.ps1 -Environment dev|prod

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet('dev', 'prod')]
    [string]$Environment = 'dev',
    
    [Parameter(Mandatory=$false)]
    [string]$Namespace = 'manufacturing-copilot',
    
    [Parameter(Mandatory=$false)]
    [string]$HuggingFaceToken
)

Write-Host "🚀 Deploying Manufacturing Copilot to Kubernetes" -ForegroundColor Green
Write-Host "Environment: $Environment" -ForegroundColor Cyan
Write-Host "Namespace: $Namespace" -ForegroundColor Cyan
Write-Host ""

# Check prerequisites
Write-Host "📋 Checking prerequisites..." -ForegroundColor Yellow

# Check kubectl
try {
    $null = kubectl version --client 2>$null
    Write-Host "✅ kubectl found" -ForegroundColor Green
} catch {
    Write-Host "❌ kubectl not found. Please install kubectl." -ForegroundColor Red
    exit 1
}

# Check helm
$helmAvailable = $true
try {
    $null = helm version 2>$null
    Write-Host "✅ helm found" -ForegroundColor Green
} catch {
    Write-Host "⚠️  helm not found. Using kubectl instead." -ForegroundColor Yellow
    $helmAvailable = $false
}

# Check cluster connection
try {
    $null = kubectl cluster-info 2>$null
    $context = kubectl config current-context
    Write-Host "✅ Connected to cluster: $context" -ForegroundColor Green
} catch {
    Write-Host "❌ Cannot connect to Kubernetes cluster. Check your kubeconfig." -ForegroundColor Red
    exit 1
}

# Get HuggingFace token
if ([string]::IsNullOrEmpty($HuggingFaceToken)) {
    Write-Host ""
    Write-Host "🔑 HuggingFace API Token Required" -ForegroundColor Yellow
    $HuggingFaceToken = Read-Host "Enter your HuggingFace token" -AsSecureString
    $HuggingFaceToken = [Runtime.InteropServices.Marshal]::PtrToStringAuto(
        [Runtime.InteropServices.Marshal]::SecureStringToBSTR($HuggingFaceToken))
    
    if ([string]::IsNullOrEmpty($HuggingFaceToken)) {
        Write-Host "❌ HuggingFace token is required" -ForegroundColor Red
        exit 1
    }
}

# Create namespace
Write-Host ""
Write-Host "📦 Creating namespace..." -ForegroundColor Yellow
kubectl create namespace $Namespace --dry-run=client -o yaml | kubectl apply -f - | Out-Null

# Deploy with Helm or kubectl
if ($helmAvailable) {
    Write-Host ""
    Write-Host "🎯 Deploying with Helm..." -ForegroundColor Yellow
    
    # Update dependencies
    Push-Location charts\manufacturing-copilot
    helm dependency update 2>$null
    Pop-Location
    
    # Deploy
    helm upgrade --install manufacturing-copilot `
        .\charts\manufacturing-copilot `
        --namespace $Namespace `
        --values .\charts\manufacturing-copilot\values-$Environment.yaml `
        --set secrets.huggingfaceToken="$HuggingFaceToken" `
        --create-namespace `
        --wait `
        --timeout 10m
    
    Write-Host "✅ Helm deployment complete!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "🎯 Deploying with kubectl..." -ForegroundColor Yellow
    
    # Create secret
    kubectl create secret generic manufacturing-copilot-secret `
        --from-literal=HUGGINGFACE_TOKEN="$HuggingFaceToken" `
        --namespace=$Namespace `
        --dry-run=client -o yaml | kubectl apply -f - | Out-Null
    
    # Apply manifests
    kubectl apply -f kubernetes\ --namespace=$Namespace
    
    Write-Host "✅ kubectl deployment complete!" -ForegroundColor Green
}

# Wait for pods
Write-Host ""
Write-Host "⏳ Waiting for pods to be ready..." -ForegroundColor Yellow
try {
    kubectl wait --for=condition=ready pod `
        --selector=app=manufacturing-copilot `
        --namespace=$Namespace `
        --timeout=5m
} catch {
    Write-Host "⚠️  Pods not ready yet. Check status with:" -ForegroundColor Yellow
    Write-Host "   kubectl get pods -n $Namespace" -ForegroundColor Cyan
    Write-Host "   kubectl logs -n $Namespace -l app=manufacturing-copilot" -ForegroundColor Cyan
}

# Display status
Write-Host ""
Write-Host "📊 Deployment Status:" -ForegroundColor Green
Write-Host "====================" -ForegroundColor Green
kubectl get deployments -n $Namespace
Write-Host ""
kubectl get pods -n $Namespace
Write-Host ""
kubectl get svc -n $Namespace

# Display access info
Write-Host ""
Write-Host "🌐 Access Information:" -ForegroundColor Green
Write-Host "=====================" -ForegroundColor Green

$ingressHost = kubectl get ingress -n $Namespace -o jsonpath='{.items[0].spec.rules[0].host}' 2>$null
if ($ingressHost) {
    Write-Host "Ingress URL: https://$ingressHost" -ForegroundColor Cyan
} else {
    Write-Host "No ingress configured. Use port-forward to access:" -ForegroundColor Yellow
    Write-Host "  kubectl port-forward svc/manufacturing-copilot 8080:8080 -n $Namespace" -ForegroundColor Cyan
    Write-Host "  Then access: http://localhost:8080" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "✨ Deployment successful!" -ForegroundColor Green
Write-Host ""
Write-Host "📚 Next steps:" -ForegroundColor Yellow
Write-Host "  - View logs: kubectl logs -n $Namespace -l app=manufacturing-copilot --tail=100" -ForegroundColor Cyan
Write-Host "  - Scale pods: kubectl scale deployment manufacturing-copilot --replicas=3 -n $Namespace" -ForegroundColor Cyan
Write-Host "  - Update config: kubectl edit configmap manufacturing-copilot-config -n $Namespace" -ForegroundColor Cyan
if ($helmAvailable) {
    Write-Host "  - Delete: helm uninstall manufacturing-copilot -n $Namespace" -ForegroundColor Cyan
} else {
    Write-Host "  - Delete: kubectl delete namespace $Namespace" -ForegroundColor Cyan
}
