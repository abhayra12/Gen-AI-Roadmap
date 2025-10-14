variable "service_name" { type = string }
variable "project_id" { type = string }
variable "region" { type = string }
variable "image_uri" { type = string }
variable "min_instances" { type = number }
variable "max_instances" { type = number }
variable "secrets" {
  description = "A map of environment variable names to secret version IDs."
  type        = map(string)
  default     = {}
}
