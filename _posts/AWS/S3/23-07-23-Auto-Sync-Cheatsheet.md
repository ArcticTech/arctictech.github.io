---
title: Auto Sync Buckets Cheatsheet
date: 2023-07-23 04:32:00 -700
categories: [Aws-s3]
tags: [aws,s3]
---

1. Create a file ```auto-sync-file.sh``` and create a folder ```auto-sync-logs``` to store the logs.

2. ```auto-sync-file.sh``` should contain the following:
```
#!/bin/bash
aws s3 sync s3://my-bucket-destination s3://my-bucket-source --source-region us-west-2 --regio
n us-west-2
```

3. Configure your crontab to the following, this will run the ```auto-sync-file.sh``` script and write the logs to ```auto-sync-logs```. Then every week it will delete the older logs.
```
*/5 * * * * /home/ec2-user/auto-sync-file.sh >> /home/ec2-user/auto-sync-logs/cron_log\_`date +20\%
y\%m\%d\%H\%M\%S` 2>&1 &
0 7 * * * /usr/bin/find /home/ec2-user/auto-sync-logs -type f -mtime +15 -exec rm -f {} \;
```
