# This module manages secrets in Google Secret Manager.

resource "google_secret_manager_secret" "secrets" {
  for_each = var.secret_data
  
  project   = var.project_id
  secret_id = each.key

  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "versions" {
  for_each = google_secret_manager_secret.secrets

  secret      = each.value.id
  secret_data = var.secret_data[each.key]
}
