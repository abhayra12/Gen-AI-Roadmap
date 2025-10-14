# scripts/deploy_cloud_run.py
import subprocess
import shlex
import argparse
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class CloudRunConfig:
    """Configuration for a Cloud Run deployment."""
    service_name: str
    image_uri: str
    region: str
    project_id: str
    max_instances: int = 4
    min_instances: int = 0
    cpu: int = 1
    memory: str = "512Mi"
    vpc_connector: str = ""
    env_vars: Dict[str, str] = field(default_factory=dict)
    secrets: Dict[str, str] = field(default_factory=dict)

def run_command(command: List[str], simulate: bool):
    """Executes a command or prints it if in simulation mode."""
    print("--- Deployment Command ---")
    # Use shlex.join for proper shell quoting
    print(shlex.join(command))
    print("--------------------------")

    if simulate:
        print("\n--- Deployment Successful (Simulated) ---")
        return

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("\n--- Deployment Successful ---")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"\n--- Deployment Failed ---")
        print(f"Return Code: {e.returncode}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        raise

def deploy_to_cloud_run(config: CloudRunConfig, simulate: bool):
    """Constructs and runs the gcloud command to deploy a service."""
    
    command = [
        "gcloud", "run", "deploy", config.service_name,
        "--image", config.image_uri,
        "--region", config.region,
        "--project", config.project_id,
        "--platform", "managed",
        "--allow-unauthenticated",
        "--min-instances", str(config.min_instances),
        "--max-instances", str(config.max_instances),
        "--cpu", str(config.cpu),
        "--memory", config.memory,
    ]
    
    if config.vpc_connector:
        command.extend(["--vpc-connector", config.vpc_connector])
        
    if config.env_vars:
        env_vars_str = ",".join([f"{key}={value}" for key, value in config.env_vars.items()])
        command.extend(["--set-env-vars", env_vars_str])

    if config.secrets:
        secret_args = ",".join([f"{env_var}={name}:latest" for name, env_var in config.secrets.items()])
        command.extend(["--update-secrets", secret_args])

    run_command(command, simulate)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy a service to Google Cloud Run.")
    parser.add_argument("--project-id", required=True, help="GCP Project ID.")
    parser.add_argument("--service-name", required=True, help="Cloud Run service name.")
    parser.add_argument("--image-uri", required=True, help="Full URI of the container image.")
    parser.add_argument("--region", required=True, help="GCP region for the deployment.")
    parser.add_argument("--simulate", action="store_true", help="Simulate the deployment without running gcloud.")
    
    args = parser.parse_args()

    # Example configuration for deploying to a staging environment
    staging_config = CloudRunConfig(
        project_id=args.project_id,
        service_name=args.service_name,
        image_uri=args.image_uri,
        region=args.region,
        min_instances=0,
        max_instances=2,
        env_vars={
            "ENVIRONMENT": "staging",
            "LOG_LEVEL": "DEBUG"
        },
        secrets={
            "API_KEY_STAGING": "ENV_API_KEY",
            "DB_PASSWORD_STAGING": "ENV_DB_PASSWORD"
        }
    )
    
    print(f"Deploying with config: {staging_config}")
    deploy_to_cloud_run(staging_config, args.simulate)
    
    # Example command to run this script:
    # python scripts/deploy_cloud_run.py \
    #   --project-id "my-gcp-project" \
    #   --service-name "copilot-api-staging" \
    #   --image-uri "gcr.io/my-gcp-project/copilot-api:sha-123abc" \
    #   --region "us-central1" \
    #   --simulate
