---
title: EC2 Basics Tutorial
date: 2023-07-23 00:00:00 -700
categories: [Aws-ec2]
tags: [aws,ec2,tutorial]
---

## EC2 Basics Tutorial
This is a basic tutorial on how to launch an Amazon Elastic Compute Cloud (EC2). EC2 is a foundational web service that offers scalable and flexible computing capacity in the cloud, allowing users to launch and manage virtual machines, known as instances. EC2 instances can be provisioned with varying sizes of CPU, memory, storage, and other specifications, providing users with complete control over their computing resources.

### Objective
Once set up, we should be able to SSH into our EC2 via the command line (Linux, MAC). For windows, PuTTY (see PuTTY guide).

In the command line:
```
ssh ec2-user@XX.XXX.XX.XXX -i /user/home/mykeys/ec2key-us-east-1.pem
```

### Configure EC2 Instance Details
To launch an EC2, go to the EC2 console and click Launch Instance.
1. Give your instance a name, ie: ```My-EC2-Instance```.
2. Select an image, ie: ```Amazon Linux AMI```.
3. Select an architecture, ie: ```64-bit (x86)```.
4. Select an instance type, ie: ```t2.micro```.

### Configure Key Pair
The key pair is what you will be using to SSH into your instance. Either select an existing keypair if you have one already created or create a new keypair. To create a new keypair do the following:
1. Click Create New Keypair.
2. Give the keypair a name, ie: ```ec2key-us-east-1```.
3. Select RSA and ```.pem``` for the format.
4. Click Create Keypair, then download the ```.pem``` file and save it locally in a secure place, ie:
```
/user/home/mykeys/ec2key-us-east-1.pem
```

### Configure Network Settings
1. Leave the assigned VPC, subnet, and auto-assign public IP as default. By default, our EC2 instance will be set up in the default virtual private cloud (VPC). It is recommended that you provision your own custom VPC. To learn how to create your own VPC see the "Setup VPC Guide". However, if you don't want to mess with networking, then leave it in the default VPC.
2. Configure security groups. This is very important. By leaving your instance in the default VPC, the only thing controlling the traffic into and out of your EC2 is its security group association. It is highly recommended that you create your own security group. If you don't already have a security group created, it is recommended to navigate to the Security Group page using the navigation bar on the left and then configure a new security group.

### Configure Security Groups
To configure a new security group, click Create Security Group. We will configure a security group that allows inbound access over port 22 only for our IP address.
1. Give your security group a name, ie: ```Home-SSH```.
2. Add a description, ie: ```Allows SSH from my home IP address.```.
3. Select the VPC you want the security group to associate with, in our case, it is just the default.
4. Under Inbound rules click add a rule and add the following rule.
```
Type = "SSH"
Protocol = "TCP"
Port range = "22"
Source = "My IP"
Description = "Allow inboud 22 from my ip address"
```
5. Under Outbound rules, allow all.
```
Type = "All traffic"
Protocol = "All"
Port range = "All"
Source = "0.0.0.0/0"
Description = ""
```
6. Tags are optional, but they can be very useful. Here are some example tags to add.
```
Key = "Name", Value = "My-EC2-Instance"
Key = "Type", Value = "t2-micro_1gig"
Key = "Department", Value = "Network Scaling Integration"
Key = "Team", Value = "Data Analytics"
Key = "Owner", Value = "John Smith"
```
7. Now click "create security group". Once created, navigate back to Launch EC2, click Select Existing Security group, and add the security group you just created.

### Configure Storage
Under Configure Storage, you can specify how much Elastic Block Storage (EBS) you want on your EC2. For our purposes, just leave this as default: ```1x 8GiB gp3 root volume (not encrypted)```.

### Configure IAM Role
Roles are a very important feature that securely allows one Aws service to talk to another AWS service without the need for managing credentials or having to worry about storing credentials within your virtual machines. We will create a role that allows EC2 full access to S3 here:

1. If you are in the IAM console, click Roles > Create Role. If you are in the EC2 console launching an instance, under Advanced Details, click Create New IAM Profile then Create Role.
2. For Trusted Entity Type select AWS service.
3. For Use Case, select EC2, and click Next.
4. Attach a policy to your role. For our purposes, select the ```AmazonS3FullAccess``` policy and click next.
5. Give the role a name, ie: ```EC2_Admin=S3```.
6. Give the role a description, ie: ```Allows EC2 admin access to S3```.
7. Leave everything else as default and click create role.
8. To use this role, simply go to your EC2 instance and add this role to your instance. Under your EC2 instance, under IAM instance profile, select this role.
9. If properly configured, once you SSH into your instance, you should be able to see the contents of your S3 bucket from your EC2 with the following command:
```
aws s3 ls
```

### Add User Data
Sometimes you may want to add user data on the startup of the instance, such as running a bash script. You can add that in the User Data section. The following is a script that will shutdown your instance after two hours. It is good to add this script to your testing instances as it will automatically turn them off so you don't have to worry about forgetting.
```
#!/bin/bash
yum update -y
echo 'shutdown -h 120' >> /etc/rc.local
```

### Launching and Accessing
Once you have your instance configured, click Launch to launch the instance. In your ec2 console you should see your instance firing up. Wait till the Instance State changes to Running, then you can SSH into your instance.

1. For linux and mac users, you will need to change the permissions on the  ```.pem``` key that you downloaded. For mac users, this may be a ```.cer``` file. To change the permissions run:
```
chmod 400 /user/home/mykeys/ec2key-us-east-1.pem
```
* For windows users, you will need to convert key pair to PuTTY key. See PuTTY Guide for instructions on this.

2. Now go to your EC2 console and find the public ip address of your EC2. For linux and mac users, SSH into your EC2 instance with the following command and replace "XX.XXX.XX.XXX" with the public ip address of your EC2.
```
ssh ec2-user@XX.XXX.XX.XXX -i /user/home/mykeys/ec2key-us-east-1.pem
```
* For windows users, see PuTTY Guide for instructions on how to SSH.
3. If you added the role, ```EC2_Admin=S3```, earlier we can test to make sure our role is working. Simply run ```aws s3 ls``` and you should be able to see the contents of your S3 bucket from your EC2.

### Result
Congrats, you have launched your first EC2 instance. Now you should be able to SSH into EC2 (for Linux and Mac) with the following command.
```
ssh ec2-user@XX.XXX.XX.XXX -i /user/home/mykeys/ec2key-us-east-1.pem
```
