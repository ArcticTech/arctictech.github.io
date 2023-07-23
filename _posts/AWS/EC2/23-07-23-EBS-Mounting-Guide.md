---
title: EBS Mounting Guide
date: 2023-07-23 00:06:00 -700
categories: [Aws-ec2]
tags: [aws,ec2,ebs]
---

## EBS Mounting Guide
After you attach an Amazon EBS volume to your instance, it is exposed as a block device. You can format the volume with any file system and then mount it. After you make the EBS volume available for use, you can access it in the same ways that you access any other volume. Any data written to this file system is written to the EBS volume and is transparent to applications using the device. See these docs for more details:
```
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html
```

### Format and mount an attached volume
1. Connect to your instance using SSH. For more information, see Connect to your Linux instance.

2. The device could be attached to the instance with a different device name than you specified in the block device mapping. For more information, see Device naming on Linux instances. Use the ```lsblk``` command to view your available disk devices and their mount points.
```
lsblk
df
```

3. Determine whether there is a file system on the volume. New volumes are raw block devices, and you must create a file system on them before you can mount and use them. Volumes that were created from snapshots likely have a file system on them already; if you create a new file system on top of an existing file system, the operation overwrites your data.
```
sudo file -s /dev/xvdf
```

4. Only if the volume is empty, use the ```mkfs -t command``` to create a file system on the volume. Important: doing this will delete any existing data on the volume.
```
sudo mkfs -t xfs /dev/xvdf
```
If you get an error that ```mkfs.xfs``` is not found, use the following command to install the XFS tools and then repeat the previous command:
```
sudo yum install xfsprogs
```

5. Create a directory and mount the volume.
```
sudo mkdir /mnt/data0
sudo mount /dev/xvdf /mnt/data0
```
Note: to unmount us the following.
```
sudo umount /mnt/data0
```

6. Grant permission on the directory
```
sudo chown -R ec2-user /mnt/data0
```

7. Check the newly mounted volume.
```
df
```
Note: if you reboot your instance you will need to remount unless you use auto-remount.

### Auto-Remount After Reboot

1. Use the ```blkid``` command to find the UUID of the device.
```
sudo blkid
/dev/xvdf: UUID="549af139-1164-47e4-bfb6-4e15e70fb5ad" TYPE="xfs"
```
For Ubuntu use:
```
sudo lsblk -o +UUID
```

2. Edit /etc/fstab to make the settings persist.
```
sudo nano /etc/fstab
```
Add the following line (note: your uuid and type):
```
UUID=549af139-1164-47e4-bfb6-4e15e70fb5ad  /mnt/data0  xfs  defaults,nofail  0  2
```
For Ubuntu use:
```
UUID=549af139-1164-47e4-bfb6-4e15e70fb5ad  /mnt/data0  xfs  defaults,nofail,nobootwait  0  2
```

3. Reboot and then check to see that your mount is still attached.
```
sudo reboot
lsblk
df
```
