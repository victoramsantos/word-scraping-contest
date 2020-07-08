provider "aws" {
  region = var.region
}

module "vpc" {
  source = "../../../../modules/aws/vpc"
  cidr_block = var.vpc_cdir_block

  tags = {
    Name = var.vpc_name
  }
}

module "internet_gateway" {
  source = "../../../../modules/aws/internet_gateway"
  tags = {
    Name = var.igw_name
  }
  vpc_id = module.vpc.vpc_id
}

module "public_subnet_a" {
  source = "../../../../modules/aws/subnet"
  cidr_block = var.cidr_pub_sb_a
  vpc_id = module.vpc.vpc_id
  is_public = true

  tags = {
    Name = var.name_pub_sb_a
  }
  az = var.public_subnet_a_az
}

module "public_subnet_b" {
  source = "../../../../modules/aws/subnet"
  cidr_block = var.cidr_pub_sb_b
  vpc_id = module.vpc.vpc_id
  is_public = true

  tags = {
    Name = var.name_pub_sb_b
  }
  az = var.public_subnet_b_az
}

module "private_subnet_a" {
  source = "../../../../modules/aws/subnet"
  cidr_block = var.cidr_private_sb_a
  vpc_id = module.vpc.vpc_id
  is_public = false

  tags = {
    Name = var.name_private_sb_a
  }
  az = var.private_subnet_a_az
}

module "private_subnet_b" {
  source = "../../../../modules/aws/subnet"
  cidr_block = var.cidr_private_sb_b
  vpc_id = module.vpc.vpc_id
  is_public = false

  tags = {
    Name = var.name_private_sb_b
  }
  az = var.private_subnet_b_az
}

module "public_route_table" {
  source = "../../../../modules/aws/route_table/route/internet_gateway"
  cidr_block = "0.0.0.0/0"
  gateway_id = module.internet_gateway.igw_id
  tags = {
    Name = var.public_route_table_name
  }
  vpc_id = module.vpc.vpc_id
}

module "public_route_table_association_a" {
  source = "../../../../modules/aws/route_table/association"
  route_table_id = module.public_route_table.route_id
  subnet_id = module.public_subnet_a.subnet_id
}

module "public_route_table_association_b" {
  source = "../../../../modules/aws/route_table/association"
  route_table_id = module.public_route_table.route_id
  subnet_id = module.public_subnet_b.subnet_id
}

module "elastic_ip_a" {
  source = "../../../../modules/aws/elastic_ip"
  internet_gateway = module.internet_gateway
}

module "nat_gateway" {
  source = "../../../../modules/aws/nat_gateway"
  eip_id = module.elastic_ip_a.elastic_ip_id
  nat_gatway_name = var.nat_gateway_a_name
  subnet_id = module.public_subnet_a.subnet_id
}

module "private_route_table" {
  source = "../../../../modules/aws/route_table/route/nat_gateway"
  cidr_block = "0.0.0.0/0"
  nat_id = module.nat_gateway.nat_gateway_id
  tags = {
    Name = var.private_route_table_name
  }
  vpc_id = module.vpc.vpc_id
}

module "private_route_table_association_b" {
  source = "../../../../modules/aws/route_table/association"
  route_table_id = module.private_route_table.route_id
  subnet_id = module.private_subnet_a.subnet_id
}

module "private_route_table_association_a" {
  source = "../../../../modules/aws/route_table/association"
  route_table_id = module.private_route_table.route_id
  subnet_id = module.private_subnet_b.subnet_id
}