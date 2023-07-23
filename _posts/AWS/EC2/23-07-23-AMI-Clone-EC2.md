---
title: AMI Clone EC2 Guide
date: 2023-07-23 00:02:00 -700
categories: [Aws-ec2]
tags: [aws,ec2]
---

## AMI Clone EC2 Guide
There is no clone feature available in AWS EC2 service. However, you can create an image of your EC2 instance and create a new instance out of that image. You can use the Amazon Machine Image (AMI) feature of EC2 service to create an image of your EC2 instance. See this guide for details:
```
https://cloudaffaire.com/faq/how-to-clone-an-aws-ec2-instance/
```

1. Select your EC2, click Action > Image and Templates > Create Image

2. Create the image with the following, then click Create Image:
```
Image Name = MyImage
No Reboot = Enable
Tag image and snapshots together = True
Key = Name
Value = MyImage
```

3. Go to Elastic Block Store > Snapshots and you can find your newly created image.

4. Go to AMIs and find the image you created. Once the status becomes available, select the image and click Action > Launch.

### Result
After launching your instance from your AMI, you will find your new EC2 instance in the EC2 console.