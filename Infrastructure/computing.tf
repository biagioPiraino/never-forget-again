terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
    }
  }
}

# Define variables
variable "env_tag" {
  default = "development"
}

variable "scope" {
  default = "automated-task"
}

variable "deployment_region" {
  default = "eu-west-1"
}

# Configure AWS provider
provider "aws" {
  region = var.deployment_region
  access_key = "" # Add an access key
  secret_key = "" # Add a secret key
}

# Ubuntu AMI lookup
data "aws_ami" "ubuntu" {
	most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

# Create security group to allow SSH from local machine
resource "aws_security_group" "ssh_security_group" {
  name = "allow-local-ssh"
  description = "Allow SSH traffic from port 22"

  # Ingress allows inbound traffics from everywhere
  # on port 22
  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Egress allows all the outbound traffic 
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create a key pair
resource "aws_key_pair" "ec2_key_pair" {
  key_name = "ec2-key-pair"
  # Supply a user-generated public key
  # In Ubuntu, you can create an SSH key by using:
  # $ ssh-keygen -t ed25519 -C "your_email@example.com"
  public_key = "" # Input user-generated key
}

# Deploy compute instance with user data
resource "aws_instance" "compute_instance" {
	ami = data.aws_ami.ubuntu.id
	instance_type = "t2.micro"
  key_name = aws_key_pair.ec2_key_pair.key_name
  security_groups = [aws_security_group.ssh_security_group.id]
	tags = {
		"name" = "compute-instance"
		"environment" = var.env_tag
		"scope" = var.scope
	}
}