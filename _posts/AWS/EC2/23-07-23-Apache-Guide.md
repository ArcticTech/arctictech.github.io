---
title: Apache Guide
date: 2023-07-23 00:05:00 -700
categories: [Aws-ec2]
tags: [aws,ec2,apache]
---

## Apache Guide
This is a guide on setting up Apache on an EC2 instance. Apache is one of the most widely used open-source web servers. It was developed and maintained by the Apache Software Foundation. Apache is designed to serve web pages and content over the internet.

### Objective
Once set up, you will be able to view publicly the ```index.html``` webpage of your EC2 from your browser by pasting in the IPv4 Public IP address. This is found in your instance dashboard (bottom left).
* Important Note: You must add HTTP and HTTPS inbound and outbound access to all traffic in your EC2's security group.

### Prerequisites
You must be in root and be sure to update your instance and install Apache.
```
sudo su
yum update
yum install httpd -y
```

Alternatively, you can also add the following script to the user data section when creating the EC2 instance. This will run the bash script upon launching the instance.
```
#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
yum install amazon-efs-utils -y
```

### Starting Apache
Start Apache and make sure it starts every time we boot up the EC2 instance.
```
service httpd start
chkconfig httpd on
```

### Create a website
1. Go to "/var/www/html", anything in this directory is publicly accessible.
```
cd /var/www/html
```
2. create an ```index.html``` with the following: ```<html><h1>Hello World</h1></html>```

### Result
Now test the result, from your browser by pasting in the IPv4 Public IP address and you should be able to view your ```index.html``` file from your browser.
