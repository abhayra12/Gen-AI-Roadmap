# terraform/modules/cloud_run/outputs.tf

output "service_url" {
  description = "The URL of the deployed service."
  value       = google_cloud_run_v2_service.default.uri
}
