---
title: S3 With Boto3
date: 2023-07-28 07:20:00 -700
categories: [Aws-s3]
tags: [aws,s3]
---

## Setup Boto3 Guide
This is a guide on accessing S3 with the Boto3 package.

### Prerequisites
Create a user in Aws IAM with at least S3 permissions. It is highly recommended that you create a group with S3 permissions and assign your user to that group. See "IAM Basics Tutorial" for more details. 

### Installing and Configuring
1. Install boto3.
```python
pip install boto3
```

2. Use ```aws configure``` to add your credentials and select your default region:
```
aws configure
```
* Configuration can look as follows:
```
AWS Access Key ID: *****
AWS Secret Access Key: *****
Default region name: us-east-1
Default output format:
```

### Using Boto3 to access S3
Now open up the Python shell and make a connection to S3 to check that your credentials are working properly. If everything is working properly it should print out all buckets you have on S3.

1. List all of your buckets with the following command:
```python
import boto3
s3 = boto3.resource("s3")
print(s3) #Expected: s3.ServiceResource()
#
for bucket in s3.buckets.all():
	print(bucket.name) #Expect to see all your buckets in S3
```

2. Also, you can create and upload new files to S3 with the following:
```python
with open("readme.txt", "w") as f:
	f.write("Hello World")
	f.write("This is a new text file!")
#
with open("readme.txt", "rb") as f:
	s3.Bucket("my-bucket").put_object(Key="readme.txt", Body=f)
```

## Conclusion
Now that you should have a basic understanding of how to use Boto3 to access S3.