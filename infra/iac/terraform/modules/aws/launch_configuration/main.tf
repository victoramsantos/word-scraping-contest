data "template_file" "user_data" {
  template = "${file("${path.module}/setup.tpl")}"
  vars = {
    FRONTEND_IMG = "${var.frontend_img}"
    BACKEND_IMG = "${var.backend_img}"
  }
}

resource "aws_launch_configuration" "lifecycle_lc" {
  name_prefix = var.name_prefix
  key_name = var.key_name
  image_id = var.ami_id
  instance_type = var.instance_type
  security_groups = var.security_groups
  user_data = data.template_file.user_data.rendered

  lifecycle {
    create_before_destroy = true
  }
}