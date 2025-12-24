terraform {
  required_version = ">= 1.5"
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
}

variable "db_password" {
  type        = string
  sensitive   = true
  description = "Postgres password"
}

resource "random_password" "airflow_fernet" {
  length  = 32
  special = false
}

output "airflow_fernet_key" {
  value     = random_password.airflow_fernet.result
  sensitive = true
}
