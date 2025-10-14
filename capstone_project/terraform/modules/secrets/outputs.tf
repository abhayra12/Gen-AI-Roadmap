# terraform/modules/secrets/outputs.tf

output "secret_versions" {
  description = "Map of secret names to their version IDs."
  value       = { for k, v in google_secret_manager_secret_version.versions : k => v.id }
  sensitive   = true
}
