variable "region" {
  default = "us-east-1"
}

variable "vpc_name" {
  default = "master-vpc-victoramorim"
}

variable "igw_name" {
  default = "master-igw"
}

variable "vpc_cdir_block" {
  default = "11.0.0.0/16"
}

variable "name_pub_sb_a" {
  default = "public_subnet_a"
}

variable "cidr_pub_sb_a" {
  default = "11.0.1.0/24"
}

variable "name_pub_sb_b" {
  default = "public_subnet_b"
}

variable "cidr_pub_sb_b" {
  default = "11.0.2.0/24"
}

variable "name_private_sb_a" {
  default = "private_subnet_a"
}

variable "cidr_private_sb_a" {
  default = "11.0.3.0/24"
}

variable "name_private_sb_b" {
  default = "private_subnet_b"
}

variable "cidr_private_sb_b" {
  default = "11.0.4.0/24"
}

variable "public_route_table_name" {
  default = "public_route_table"
}

variable "private_route_table_name" {
  default = "private_route_table"
}

variable "nat_gateway_a_name" {
  default = "nat_gateway_a"
}

variable "private_subnet_b_az" {
  default = "us-east-1b"
}

variable "private_subnet_a_az" {
  default = "us-east-1a"
}

variable "public_subnet_b_az" {
  default = "us-east-1b"
}

variable "public_subnet_a_az" {
  default = "us-east-1a"
}
