variable "region" {
  default = "us-east-1"
}

variable "lc_name_prefix" {
  default = "lc-victoramorim"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "ec2_key_pair" {
}

variable "create_before_destroy" {
  default = true
}

variable "ag_name_prefix" {
  default = "ag-victoramorim"
}

variable "min_size" {
  default = "1"
}
variable "max_size" {
  default = "1"
}

variable "vpc_id" {
}

variable "public_subnets" {
}

variable "tg_port" {
  default = 8000
}

variable "tg_protocol" {
  default = "HTTP"
}

variable "health_path" {
  default = "/health"
}
variable "hc_port" {
  default = 8000
}
variable "hc_threshold" {
  default = 6
}
variable "hc_unhealthy_threshold" {
  default = 8
}
variable "hc_timeout" {
  default = 2
}
variable "hc_interval" {
  default = 5
}
variable "hc_status_code" {
  default = "200"
}

variable "env_prefix" {
  default = "blue"
}

variable "appname" {
  default = "wscraping"
}

variable "frontend_img" {

}

variable "backend_img" {

}