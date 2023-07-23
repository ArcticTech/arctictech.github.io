---
title: AWS CLI Commands Cheat Sheet
date: 2023-07-20 02:02:00 -700
categories: [Aws-cli]
tags: [aws,aws-cli,cheatsheet]
---

## Aws CLI Cheatsheet
These are some of the most useful commands in the AWS CLI. See this documentation for details:
```
https://docs.aws.amazon.com/cli/latest/reference/ec2/index.html
```

1. S3 Commands.
* Lists directories in the S3 service.
```
aws s3 ls
```
* Create a bucket
```
aws s3 mb s3://mybucket
```
* Copy a file into S3
```
aws s3 cp /Users/me/Documents/myfile.txt s3://mybucket/myfiles/myfile.txt
```
* Copy a file out of S3
```
aws s3 cp s3://mybucket/myfiles/myfile.txt /Users/me/Documents/myfile.txt
```
* Copy all files out of S3
```
aws s3 cp s3://mybucket/Database_Storage/csv_10_Oct . --recursive
```

2. EC2 Commands
* Describe EC2 Instances
```
aws ec2 describe-instances
```
* Describe images
```
aws ec2 describe-images --owners amazon --filters "Name=platform,Values=linux" "Name=root-device-type,Values=ebs"
```
* Run Instances
```
aws ec2 run-instances --image-id ami-0b33d91d --count 1 --instance-type t2.micro --key-name NSI_EC2_AccessKey --security-group-ids sg-342cea4b --subnet-id subnet-df1835f2
```
* Terminate Instances
```
aws ec2 terminate-instances --instance-ids i-08d7d0264926c57aa
```
