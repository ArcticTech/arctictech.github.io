---
title: DDB Policies
date: 2023-07-20 03:05:00 -700
categories: [Aws-iam]
tags: [aws,iam]
---

## DDB Policies
* DDB Read Write Policy:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DynamoDBIndexAndStreamAccess",
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetShardIterator",
                "dynamodb:Scan",
                "dynamodb:Query",
                "dynamodb:DescribeStream",
                "dynamodb:GetRecords",
                "dynamodb:ListStreams"
            ],
            "Resource": [
                "arn:aws:dynamodb:us-east-1:XXXXXXXXXXXX:table/Users/index/*",
                "arn:aws:dynamodb:us-east-1:XXXXXXXXXXXX:table/Users/stream/*"
            ]
        },
        {
            "Sid": "DynamoDBTableAccess",
            "Effect": "Allow",
            "Action": [
                "dynamodb:BatchGetItem",
                "dynamodb:BatchWriteItem",
                "dynamodb:ConditionCheckItem",
                "dynamodb:PutItem",
                "dynamodb:DescribeTable",
                "dynamodb:DeleteItem",
                "dynamodb:GetItem",
                "dynamodb:Scan",
                "dynamodb:Query",
                "dynamodb:UpdateItem"
            ],
            "Resource": "arn:aws:dynamodb:us-east-1:XXXXXXXXXXXX:table/Users"
        },
        {
            "Sid": "DynamoDBDescribeLimitsAccess",
            "Effect": "Allow",
            "Action": "dynamodb:DescribeLimits",
            "Resource": [
                "arn:aws:dynamodb:us-east-1:XXXXXXXXXXXX:table/Users",
                "arn:aws:dynamodb:us-east-1:XXXXXXXXXXXX:table/Users/index/*"
            ]
        }
    ]
}
```
