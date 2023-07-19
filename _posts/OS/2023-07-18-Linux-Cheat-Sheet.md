---
title: Linux Cheat Sheet
date: 2023-07-18 06:00:00 -700
categories: [OS,Linux]
tags: [linux,command-line,cheat-sheat]
---

## Linux Basic Command Line Cheat Sheet

1. Basic commands: navigating, go back, list directories, print working directory.
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