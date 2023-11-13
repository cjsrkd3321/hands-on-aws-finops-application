# EC2Volumes
resource "aws_ebs_volume" "this" {
  count = 10

  availability_zone = "${var.region}a"
  size              = 1
}
