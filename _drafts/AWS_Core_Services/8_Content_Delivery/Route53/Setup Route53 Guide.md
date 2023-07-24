## Setup Route53 Guide
This is a guide on setting up a domain with Route53 on Amazon Web Services.

### Objective
The goal of this guide is to gain a good understanding of the proper way to register a domain and deploy it. We will be using Route53 for both the domain registration and configuring its routing policies.

With this guide you will configure a domain that users can use to access your website from all over the world using different routing policies and you will have the ability to test them. 

Once set up, you should be able to type your domain into your browser and access your webpage. 

### Prerequisites
In order do this guide you must have knowledge of how to set up an EC2 instance. See Setup EC2 Guide for more details.

### Register Domain
1. Go to Route53 in the console and click on Register Domain.
2. Type in a domain name, click check, and continue.
```
pathfinder.io
```
3. Fill out the registration detail and click continue.
4. Next read and accept the terms and conditions and click complete purchase.
5. Domain names may take up to three days to be ready. Once it's ready it will appear in the Registered Domains section and in Hosted Zone.

### Provision EC2 Instances
Next we will provision three EC2 instances in three different regions for testing the latency of our domain. First instance provision it in the region closes to you, in our case it's Northern Virginia. Second instance provision it in a region farthest away from you, in our case Singapore. Third instance, pick a region in between, Stockholm.

See Setup EC2 Guide for details on how to set up EC2 instances. To switch regions simply change the region on the top right of the dashboard. When provisioning each instance, add the following bootstrap script during setup (replace the XXX with the region):
```
#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
cd /var/www/html
echo "<html><h1>This is what the webpage looks like from XXX Region</h1></html>" > index.html
```

Once your three instances are setup, take note of each one's public IP address and paste them in a notepad, we will need them later.
```
3.93.15.112
13.229.231.246
13.48.132.29
```

### Result
Depending on how you configured your routing, you should be able to go to your domain and be able to connect to your web server. Simple type your domain into your browser (in our case: pathfinder.io) and you should be able to see your web page.
