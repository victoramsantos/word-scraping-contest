variable "name_prefix" {}
variable "security_groups" {}
variable "instance_type" {}
variable "key_name" {}
variable "ec2_name" {
  default = "Cluster"
}
variable "ami_id" {
  default = "ami-09d95fab7fff3776c"
}
variable "create_before_destroy" {
  default = false
}

variable "backend_img" {
}

variable "frontend_img" {
}