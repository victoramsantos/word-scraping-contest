variable "health_check_path" {
  default = ""
}
resource "aws_lb_target_group" "target_group" {
  port     = var.tg_port
  protocol = var.tg_protocol
  vpc_id   = var.vpc_id

  health_check {
    path = var.hc_path
    port = var.hc_port
    healthy_threshold = var.hc_threshold
    unhealthy_threshold = var.hc_unhealthy_threshold
    timeout = var.hc_timeout
    interval = var.hc_interval
    matcher = var.hc_status_code
  }
}
