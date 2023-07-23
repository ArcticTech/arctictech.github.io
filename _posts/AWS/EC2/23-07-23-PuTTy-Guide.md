---
title: PuTTy Guide
date: 2023-07-23 00:01:00 -700
categories: [Aws-ec2]
tags: [aws,ec2,windows,putty]
---

## PuTTy Guide
This guide is for Windows users to use PuTTy to access your EC2 instance or Lightsail instances. PuTTY is an open-source terminal emulator, serial console, and network file transfer application. It is mainly used to establish SSH connections to Linux-based remote servers and network devices like EC2 from a Windows operating system.

### Objective
Once set up, you will be able to access EC2 or Lightsail via PuTTy:
1. Select "saved session", ie: "ec2-user@XX.XXX.XX.XXX".
2. Load and Open.

### Prerequisites
1. Launch your instance. See the "EC2 Basics Tutorial" or "Lightsail Guide" for details.
2. After clicking launch, in the pop-up window, create a new key pair and download the file. This should be a .pem file. Note the download location.
3. Go ahead and hit Launch Instance.
4. Download PuTTy client from http://www.putty.org/. You will need both the PuTTy client and PuTTyGen.
5. Create a desktop shortcut for the PuTTY launcher and the PuTTYgen launcher.

### Creating PuTTy Key
Before we can connect to our instance with PuTTy, we need to create a PuTTy key from our ```.pem``` key we downloaded. See the "EC2 Basics Tutorial" or "Lightsail Guide" for details.
1. Go to PuTTyGen, click Load and find the ```.pem``` key you downloaded.
2. Click "Save Private Key", and give it a name, ie: ```ec2key-us-east-1.ppk```. We will be using this ```.ppk``` key to SSH into our instance.

### Set up PuTTy Session
Now we need to set up a connection between EC2 or Lightsail and PuTTy.

1. Open your EC2 or Lightsail instance and find the IPv4 Public IP address.
2. In PuTTy, under the Sessions category in the "Host Name (or IP address)" create a session name. The session name should be the image username and your IPv4 Public IP address. For example: If you are using an Amazon AMI the user name is ec2-user@. For ubuntu it's ubuntu@.
```
ec2-user@XX.XXX.XX.XXX
```

3. Under category click the + next to SSH, under that click on Auth. In the "Private key file for authentication" click browse and select the ```ec2key-us-east-1.ppk```.
4. Go back to "session", click save to save the session.
2. Now click Load and Open to connect to your instance.

### Result
If configured properly, you should now be able to connect to your EC2 or Lightsail instance via PuTTy.
