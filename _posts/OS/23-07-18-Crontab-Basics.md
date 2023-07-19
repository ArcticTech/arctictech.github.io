---
title: Crontab Basics
date: 2023-07-18 07:00:00 -700
categories: [OS,Linux]
tags: [linux,command-line,crontab]
---

## Crontab Basics
To schedule jobs in Linux, use crontab. For more details, see this YouTube guide: https://www.youtube.com/watch?v=QZJ1drMQz1A

### Setting up a Cron Job
To setup a cron job use the following commands.

1. Use the following command to edit your existing crontab jobs, if any.
```
crontab -e
```

2. Once you create a job and save it, use this command to list the jobs that are active.
```
crontab -l
```

### Creating a Cron Job
1. After running ```crontab -e```, add your command to the file. Here is an example command that runs Every Hour, on the hour Monday through Friday. See this link to read the cron job: https://crontab.guru/#0_0_*_*_1-5. Then this script writes the logs to this log file with a date and time: ```/home/ec2-user/xlogs/tvcron-`date +\%Y\%m\%d\%H\%M\%S`.log```.
```
0 0 * * 1-5 ./tradingview_automator.py >> /home/ec2-user/xlogs/tvcron-`date +\%Y\%m\%d\%H\%M\%S`.log 2>&1
```

2. To automate removing your older log files, add this command to crontab. This removes any file older than 10 days.
```
0 7 1,15 * * find /home/ec2-user/xlogs/tvcron-* -type f -mtime +10 | xargs rm
```
