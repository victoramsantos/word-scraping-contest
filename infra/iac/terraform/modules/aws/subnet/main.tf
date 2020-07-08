resource "aws_subnet" "subnet" {
  vpc_id     = var.vpc_id
  cidr_block = var.cidr_block
  tags = var.tags
  map_public_ip_on_launch = var.is_public
  availability_zone = var.az
}