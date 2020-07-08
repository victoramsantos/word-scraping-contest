resource "aws_lb" "alb" {
  name        = var.name
  internal           = false
  load_balancer_type = "application"
  security_groups    = var.security_groups
  subnets            = var.subnets
}

resource "aws_lb_listener" "front_end" {
  load_balancer_arn = aws_lb.alb.arn
  port              = "80"

  default_action {
    type             = "forward"
    target_group_arn = var.target_group
  }
}