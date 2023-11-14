# EC2Volumes
resource "aws_ebs_volume" "this" {
  availability_zone = "${var.region}a"
  size              = 1
}
