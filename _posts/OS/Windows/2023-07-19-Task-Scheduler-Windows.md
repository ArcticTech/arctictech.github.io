---
title: Task Scheduler Windows
date: 2023-07-19 00:00:00 -700
categories: [OS,Windows]
tags: [windows,windows-tricks]
---

## Task Scheduler for Windows
This is a guide on using the task scheduler on Windows.

1. Use ```schtasks``` for help.
```
schtasks -? 
```

2. List out scheduled tasks. Use -tn to find a specific task.
```
schtasks -query -fo list -v -tn "test_automate_extract"
```

### Creating Tasks
1. Create a task. Notes: tn = task name, tr = task location, sc = how often, st = start time. 
```
schtasks -create -tn "test_automate_extract" -tr /c/Users/Hello/Documents/WorkPro~1/11Auto~1/hello_world.sh -sc daily -st 03:47:00
```

2. Note: if directories have spaces use the shorthand of the file name. For example "Work Projects" would be "WorkPro~1". The following command will give you a list of all the shorthand file names in the "Documents" directory:
```
dir /X ~1 C:\Users\Hello\Desktop\
```

3. Change the task with:
```
schtasks -change -tn "test_automate_extract" -st 22:11
```

4. Delete the task. Use f to bypass the warning.
```
schtasks -delete -tn "test_automate_extract" -f
```