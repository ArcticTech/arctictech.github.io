---
title: GUI for EC2 Guide
date: 2023-07-23 00:03:00 -700
categories: [Aws-ec2]
tags: [aws,ec2]
---

## GUI for EC2 Guide
This guide will go over how to use a GUI with an Amazon Linux EC2 instance. See this guide for details:
```
https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-2-install-gui/
```

### Install TigerVNC on Your Local Machine
Visit the [TigerVNC website](https://tigervnc.org/) for detailed installation instructions. For Mac OS go look for the following:
```
TigerVNC-1.12.0.dmg
```

### Install MATE on Your EC2
MATE is a lightweight GUI based on GNOME 2 available as an extra for Amazon Linux 2.

1. Install MATE packages.
```
sudo amazon-linux-extras install mate-desktop1.x
```
2. Define MATE as your default desktop for all users.
```
sudo bash -c 'echo PREFERRED=/usr/bin/mate-session > /etc/sysconfig/desktop'
```

### Install and Setup TigerVNC on Your EC2
TigerVNC will allow us to access EC2 via a GUI.

1. Install TigerVNC.
```
sudo yum install tigervnc-server
```

2. Restrict VNC access to the local host so that VNC can only be accessed through a tunnel.
```
sudo mkdir /etc/tigervnc
sudo bash -c 'echo localhost > /etc/tigervnc/vncserver-config-mandatory'
```

### Start TigerVNC
Start TigerVNC on display 1 so that the service starts automatically at boot time.

1. Copy from the vncserver template from TigerVNC to your system:
```
sudo cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@.service
```

2. Replace any occurrences of ```user``` with ```ec2-user``` using the following command:
```
sudo sed -i 's/<USER>/ec2-user/' /etc/systemd/system/vncserver@.service
```

3. Reload the ```systemctl```.
```
sudo systemctl daemon-reload
```

4. Enable and start the service.
```
sudo systemctl enable vncserver@:1
sudo systemctl start vncserver@:1
```

5. Run ```vncserver```. If it prompts you, setup a password for VNC and for view-only password press n for no.
```
vncserver
```

### Connecting to TigerVNC

1. Open a new connection to your EC2 instance and enable port forwarding.
```
ssh -L 5901:localhost:5901 -i /user/home/mykeys/ec2key-us-east-1.pem ec2-user@XX.XX.XX.XX
```

2. Open TigerVNC on your local machine and connect to the VNC server via:
```
localhost:1
```

### Additional Tools

What's the point of having a UI if you don't have a browser? To install Firefox use the following command:
```
sudo amazon-linux-extras install firefox
```

### Result
Now you should be able to access the VNC server using an encrypted SSH tunnel and be able to use your GUI with your EC2 instance.
