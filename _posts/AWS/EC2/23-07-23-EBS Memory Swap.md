---
title: EBS Memory Swap
date: 2023-07-23 00:07:00 -700
categories: [Aws-ec2]
tags: [aws,ec2,ebs]
---

## EBS Memory Swap Guide
Swap space in Linux can be used when a system requires more memory than it has been physically allocated (RAM). When swap space is enabled, Linux systems can swap infrequently used memory pages from physical memory to swap space (either a dedicated partition or a swap file in an existing file system) and free up that space for memory pages that require high-speed access.

In order to do this guide, you will need to create an EBS Volume and attach the EBS Volume to your EC2 instance.

1. Run ```lsblk ``` to check new volume, it will appear as ```/dev/xvdc``` on instance.
```
$ lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
xvda    202:0    0  256G  0 disk
└─xvda1 202:1    0  256G  0 part /
xvdc    202:80   0   32G  0 disk
```

2. Allow access to volume.
```
sudo chmod 600 /dev/xvdc
```

3. Set up the swap area.
```
sudo mkswap /dev/xvdc
```

4. Enable swap.
```
sudo swapon /dev/xvdc
```

5. Edit ```/etc/fstab``` to make the settings persist.
```
sudo nano /etc/fstab
```
Add the following line:
```
/dev/xvdc none swap sw 0 0
```

6. Reboot.
```
sudo reboot
lsblk
df
```

7. Check swap space.
```
sudo swapon --show
NAME      TYPE      SIZE   USED PRIO
/dev/xvdf partition  32G 279.9M   -1
```
