---
title: Cross Region and Cross Account Replication
date: 2023-07-23 04:30:00 -700
categories: [Aws-s3]
tags: [aws,s3]
---

## Cross-Region and Cross-Account Replication
This is a guide on configuring Cross Region Replication and Cross Account Replication on your S3 bucket, to allow you to replicate the contents of your S3 bucket from one region to another or from one account to another. Note: as of June 2020 you cannot replicate multiple buckets in multiple regions or accounts.

### Objective
Once set up, we should have a good understanding of the process of using Cross Region and Cross Account Replication to replicate your objects in buckets from one region to another region or account.

### Cross-Region Replicate
For this, we will need to setup two S3 buckets in two different regions in the same account.

1. Create ```my-us-east-1``` bucket in ```us-east-1``` and create ```my-us-west-2``` bucket in ```us-west-2```.
2. Activate Versioning in BOTH buckets. Properties > Versioning > Enable Versioning.
3. Then, in your ```my-us-east-1``` bucket, go to Management > Replication Rules, click Create Replication Rules.
4. Configure as follows. Leave everything else as default and click "Create".
```
Set Source = "Apply to all objects in the bucket"
Destination = "Choose a bucket in this account"
Bucket Name = "my-us-west-2"
IAM role = "Create New Role"
Rule name = "cross-region-rule"
```
5. Now drop a file into your ```my-us-east-1``` bucket and you should see a copy of it appear in your ```my-us-west-2``` bucket.

### Cross-Account Replicate
Creating cross-account replication is slightly more complicated. We will need to setup two S3 buckets in two different accounts, no matter which regions you put them in.

1. Create ```my-source-account``` bucket in your Source Account and create ```my-destination-account``` bucket in your Destination Account.
2. In IAM, create a new S3 role in your Source Account. Do not attach any policies to it.
```
Role Name = "s3-cross-account-rep"
```
3. Activate Versioning in both buckets. Properties > Versioning > Enable Versioning.
4. In your ```my-source-account``` bucket, go to Management > Replication > Add Rule.
5. In the Replication Rule pop up configure as follows.
```
Set Source = "Entire bucket"
Bucket in another account = "True"
Account ID = <DESTINATION ACCOUNT NUMBER>
Bucket name = "my-destination-account"
IAM role = "s3-cross-account-rep"
Rule name = "cross-account-rule"
```
6. When you get the "Configure rule options" step, copy the bucket policy that is generated. It should look like the following.
```json
{
    "Version": "2008-10-17",
    "Id": "S3-Console-Replication-Policy",
    "Statement": [
        {
            "Sid": "S3ReplicationPolicyStmt1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<SOURCE ACCOUNT NUMBER>:root"
            },
            "Action": [
                "s3:GetBucketVersioning",
                "s3:PutBucketVersioning",
                "s3:ReplicateObject",
                "s3:ReplicateDelete"
            ],
            "Resource": [
                "arn:aws:s3:::my-destination-account",
                "arn:aws:s3:::my-destination-account/*"
            ]
        }
    ]
}
```
7. Go to your ```my-destination-account``` in your Destination Account, go to Permissions > Bucket Policy, paste in the bucket policy and click "Save".
8. Go back to your Replication rule setup in your Source Account, leave everything else as default and click "Create".
9. Now drop a file into your ```my-source-account``` bucket and you should see a copy of it appear in your ```my-destination-account``` bucket.

### Result
With this, we should have a good understanding of using Cross Region and Cross Account Replication.
