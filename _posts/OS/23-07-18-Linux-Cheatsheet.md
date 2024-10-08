---
title: Linux Cheatsheet
date: 2023-07-18 06:00:00 -700
categories: [OS,Linux]
tags: [linux,command-line,cheatsheet]
---

## Linux Basic Command Line Cheatsheet
This is a cheatsheet of some basic linux commands.

### Basic commands
1. Navigating, go back, list directories, print working directory.
```
cd /Users/Hello/Documents/
cd ..
ls
pwd
```

2. Create a file. If already exists, then select that file or directory.
```
touch example.txt
```

3. Create a directory.
```
mkdir example_folder
```

4. Move file to directory.
```
mv example.txt ./example_folder/example.txt
```

5. Remove file, remove directory.
```
rm example.txt
rmdir example_folder
```

6. List User.
cat /etc/passwd

7. Permissioning: change ownership of a folder.
```
sudo chown stephen ./example_folder
```

8. Grant permission to execute a file.
```
chmod 700 example.ch
```

9. Editing a file using Vim.
```
vim example.txt
```

10. Basic Vim commands:
```
Press i to enter insert mode.
Press esc to go back to command mode.
Type :w followed by enter to save.
Type :q followed by enter to quit.
Type :q! followed by enter to force quit.
Type gg dG to delete all.
```

11. Delete Swap Files:
```
find . -type f -name "*.sw[klmnop]" -delete
```

12. Check if a process is still running:
```
ps aux | grep <script_name>
```
Here are the different states:
* R: Running
* S: Sleeping
* T: Stopped
* Z: Zombie (terminated but not fully cleaned up)
* D: Uninterruptible sleep (usually related to I/O operations)

12. To kill a process use the following. Note, in general, you don't want to kill a process in the ```S+``` state because it is waiting for an event to complete.
```
kill <Process ID>
```
To force kill all events associated with your script:
```
pkill -f <script_name>
```

### Ubuntu
1. Updating Ubuntu.
```
sudo apt update
sudo apt full-upgrade
sudo apt-get dist-upgrade
```
2. Auto-installing critical updates.
```
sudo apt-get install unattended-upgrades -y
sudo dpkg-reconfigure -plow unattended-upgrades
```
3. Clean system:
```
su -
apt autoremove -y && apt autoclean && apt clean
```