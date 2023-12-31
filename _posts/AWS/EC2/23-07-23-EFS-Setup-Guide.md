---
title: EFS Setup Guide
date: 2023-07-23 00:04:00 -700
categories: [Aws-ec2]
tags: [aws,ec2,efs]
---

## EFS Setup Guide
This is a guide on setting up Elastic File System (EFS) for your EC2 instances. EFS is a scalable, fully managed file storage service provided by Amazon Web Services (AWS). It offers a simple and scalable solution to store and share files across multiple EC2 instances.

### Objective
The goal of this guide is to gain a good understanding of the proper way to create an elastic file system.
- Multiple EC2 instances can share one EFS
- Storage capacity is elastic meaning it will grow and shrink based on need.
- Great way to share files between EC2

Once set up, you will be able to create a file in one EC2 instance and it will be immediately replicated in the second EC2 instance.

### Prerequisites
To do this guide you must have TWO running instances of EC2 with Apache installed on the instances. See Setup EC2 Guide and Apache Guide for more details.

### Provisioning EFS
1. On the EFS Dashboard click on Create EFS.
2. In Configure file system access: select the same VPC as the EC2 instances. Note AZs that it's spread across and its security group, in our case it's ```sg-3c878a40 - default```. Then hit next.
3. Add a name.
4. Enable Lifecycle Management -> set to 14 days, automatically moves files to infrequently accessed.
5. Enable Encryption of data, then leave rest as default and hit next.
6. Click create file system.

### Enable NFS in Security Group
Note the security group that you provisioned the file system into, in the above case it's sg-3c878a40 - default. Go to the security group ```sg-3c878a40 - default```, then allow NFS inbound traffic for the security group of your EC2 Instances in our case it's ```sg-0d16dbdea2f846f5f```:
```
Type = NFS
Protocol = TCP
Port Range = 2049
Source = sg-0d16dbdea2f846f5f (Note: the security group of your EC2 Instances)
```

### Open and Check Apache for Instances
1. SSH into your EC2 instance. See Setup EC2 Guide for details. If you're on Windows PuTTY into your EC2. See PuTTy Key Guide for details.
```
ssh ec2-user@XX.XXX.XX.XXX -i /user/home/mykeys/ec2key-us-east-1.pem
```
2. Elevate privileges to root.
```
sudo su
```
3. Check to make sure that Apache is installed by making sure ```/var/www/html``` exists. This was a prerequisite.
```
cd /var/www/html
```
4. Then go to ```/var/www```
```
cd /var/www
```
5. Repeat steps 1 through 4, for the other EC2 instance. In our case it's ```ec2-user@YY.YYY.YY.YYY```

### Mounting EFS to EC2 Instances
Now that we have checked our instances, we can mount our EFS to our two EC2 instances.

1. On the EFS Dashboard, select the EFS that you provisioned and click on "Amazon EC2 mount instructions (from local VPC)"

2. Scroll down to find the ```tls``` command, which will encrypt data in transit, this should look like the following:
```
sudo mount -t efs -o tls fs-ac79922d:/ efs
```
3. Go to your first instance: ec2-user@XX.XXX.XX.XXX and paste in the above command but change "efs" to ```/var/www/html``` Note: Make sure you have installed the amazon-efs-utils. If it hangs for more than a minute then there may be an issue with your security group or network acl.
```
sudo yum install -y amazon-efs-utils
sudo mount -t efs -o tls fs-ac79922d:/ /var/www/html
```
4. Repeat step 3 for the second instance: ec2-user@YY.YYY.YY.YYY

### Result
Now that we have mounted our EFS to our two EC2 instances, we should be able to make edits to one ```/var/www/html``` directory and those changes should be replicated in the other. To test this do the following:

1. In the ```/var/www/html``` of your first EC2 Instance, ```XX.XXX.XX.XXX```, create an ```index.html``` with this "Hello World" HTML (replace ```&lt;``` with ```<```).
```html
&lt;html>
&lt;body>
&lt;h1>Hello World&lt;/h1>;
&lt;/body>;
&lt;/html>;
```
2. Then go to your second EC2 Instance ```ec2-user@YY.YYY.YY.YYY``` then navigate to ```/var/www/html``` then ls and yous should see the same ```index.html```.
```
cd /var/www/html
ls
```

