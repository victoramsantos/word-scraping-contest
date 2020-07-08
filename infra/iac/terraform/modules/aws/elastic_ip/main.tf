resource "aws_eip" "elastic_ip" {
  vpc      = true
  depends_on = [var.internet_gateway]
}