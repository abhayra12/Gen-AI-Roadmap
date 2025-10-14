variable "project_id" {
  description = "The GCP project ID to deploy resources into."
  type        = string
}

variable "region" {
  description = "The GCP region for the deployment."
  type        = string
  default     = "us-central1"
}

variable "image_uri" {
  description = "The full URI of the Docker image to deploy."
  type        = string
}

variable "max_instances" {
  description = "The maximum number of instances for the Cloud Run service."
  type        = number
  default     = 4
}

variable "min_instances" {
  description = "The minimum number of instances for the Cloud Run service."
  type        = number
  default     = 0
}

variable "openai_api_key_value" {
  description = "The value for the OpenAI API key secret."
  type        = string
  sensitive   = true
}

variable "db_password_value" {
  description = "The value for the database password secret."
  type        = string
  sensitive   = true
}
