---
title: Secrets Manager Policies
date: 2023-07-20 03:08:00 -700
categories: [Aws-iam]
tags: [aws,iam]
---

## Secrets Manager Policies
* Secrets Manager Read Only Policy:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetResourcePolicy",
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret",
                "secretsmanager:ListSecretVersionIds"
            ],
            "Resource": "arn:aws:secretsmanager:us-east-1:XXXXXXXXXXXX:secret:test-api-key-92j430"
        },
        {
            "Effect": "Allow",
            "Action": "secretsmanager:ListSecrets",
            "Resource": "*"
        }
    ]
}
```