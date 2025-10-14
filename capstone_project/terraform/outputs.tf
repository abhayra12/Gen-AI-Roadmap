# terraform/outputs.tf

output "cloud_run_service_url" {
  description = "The URL of the deployed Cloud Run service."
  value       = module.copilot_service.service_url
}

output "secret_versions" {
  description = "The full IDs of the created secret versions."
  value       = module.secrets.secret_versions
  sensitive   = true
}
