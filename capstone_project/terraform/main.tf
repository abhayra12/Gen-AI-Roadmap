terraform {
  required_version = ">= 1.5.0"

  # Configure the backend to store state in a GCS bucket
  # This is critical for team collaboration and state locking.
  backend "gcs" {
    bucket = "manufacturing-copilot-tf-state"
    prefix = "prod" # Use 'staging' or 'prod' depending on the workspace
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# --- Resources ---

# Call the reusable module to create our Cloud Run service
module "copilot_service" {
  source = "./modules/cloud_run"

  # Pass variables to the module
  service_name  = "manufacturing-copilot-api"
  project_id    = var.project_id
  region        = var.region
  image_uri     = var.image_uri
  max_instances = var.max_instances
  min_instances = var.min_instances
  
  # Pass the secret configurations to the module
  secrets = {
    "ENV_OPENAI_API_KEY" = module.secrets.secret_versions["openai-api-key"].id,
    "ENV_DB_PASSWORD"    = module.secrets.secret_versions["db-password"].id
  }
}

# Call the module to manage our secrets
module "secrets" {
  source = "./modules/secrets"

  project_id = var.project_id
  secret_data = {
    "openai-api-key" = var.openai_api_key_value,
    "db-password"    = var.db_password_value
  }
}
