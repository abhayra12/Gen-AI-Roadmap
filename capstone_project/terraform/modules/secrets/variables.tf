variable "project_id" {
  description = "The GCP project ID where secrets will be created."
  type        = string
}

variable "secret_data" {
  description = "A map where keys are secret IDs and values are the secret content."
  type        = map(string)
  sensitive   = true
  default     = {}
}
