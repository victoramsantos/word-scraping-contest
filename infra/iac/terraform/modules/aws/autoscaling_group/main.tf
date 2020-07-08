resource "aws_autoscaling_group" "default_ag" {
  name_prefix = var.name_prefix
  launch_configuration = var.launch_configuration_name
  min_size = var.min_size
  max_size = var.max_size
  vpc_zone_identifier = var.vpc_zone_identifier
  target_group_arns = var.target_group_arns

  lifecycle {
    create_before_destroy = true
  }
}