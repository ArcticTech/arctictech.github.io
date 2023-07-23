---
title: AWS CLI Find Unused Security Groups
date: 2023-07-23 12:01:00 -700
categories: [Aws-cli]
tags: [aws,aws-cli]
---

## AWS CLI Find Unused Security Groups
There are times when your architecture becomes too complex, and you need to find orphan security groups to get rid of them. the console. This guide will show you how to easily find the orphaned security groups with the CLI. See this post for details:
```
https://stackoverflow.com/questions/24685508/how-to-find-unused-amazon-ec2-security-groups
```

1. Get all security groups:
```
aws ec2 describe-security-groups --query 'SecurityGroups[*].GroupId'  --output text | tr '\t' '\n'
```
2. Get all security groups tied to an instance:
```
aws ec2 describe-instances --query 'Reservations[*].Instances[*].SecurityGroups[*].GroupId' --output text | tr '\t' '\n' | sort | uniq
```
3. Get all orphaned security groups. This command compares the two lists and finds the difference.
```
comm -23  <(aws ec2 describe-security-groups --query 'SecurityGroups[*].GroupId'  --output text | tr '\t' '\n'| sort) <(aws ec2 describe-instances --query 'Reservations[*].Instances[*].SecurityGroups[*].GroupId' --output text | tr '\t' '\n' | sort | uniq)
```