# This module defines a reusable Google Cloud Run service.

resource "google_cloud_run_v2_service" "default" {
  name     = var.service_name
  location = var.region
  project  = var.project_id

  template {
    containers {
      image = var.image_uri
      
      # Dynamically create environment variables from the secrets map
      dynamic "env" {
        for_each = var.secrets
        content {
          name = env.key
          value_from {
            secret_key_ref {
              secret  = split("/", env.value)[3] # Extract secret name from full ID
              version = split("/", env.value)[5] # Extract version from full ID
            }
          }
        }
      }
    }

    scaling {
      min_instance_count = var.min_instances
      max_instance_count = var.max_instances
    }
  }
}

# IAM policy to allow unauthenticated access to the service
resource "google_cloud_run_v2_service_iam_member" "noauth" {
  project  = google_cloud_run_v2_service.default.project
  location = google_cloud_run_v2_service.default.location
  name     = google_cloud_run_v2_service.default.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
