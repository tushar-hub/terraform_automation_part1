provider "aws" {
  region = "ap-south-1"
}

 #sqs queue connectionbucket

resource "aws_sqs_queue" "my_queue" {
  name = "my_queue1"
}

#S3 Bucket Creation
resource "aws_s3_bucket" "my_bucket" {
  bucket = "tusharbt1998"
 
}

#secret testing
resource "aws_secretsmanager_secret" "my_secret" {
  name        = "my_secret1"
  description = "A secret for the application"
}

resource "aws_secretsmanager_secret_version" "my_secret_version" {
  secret_id     = aws_secretsmanager_secret.my_secret.id
  secret_string = jsonencode({ key = "123456789" })  # Replace with your actual secret
}

#Ec2 instance initiliazation

resource "aws_instance" "my_instance" {
  ami           = "ami-08bf489a05e916bbd"  # Replace with an appropriate AMI ID
  instance_type = "t2.micro"
key_name = "tushartest"  

  tags = {
    Name = "MyInstance"
  }
}