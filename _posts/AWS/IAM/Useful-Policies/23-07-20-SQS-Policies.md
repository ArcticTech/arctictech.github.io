---
title: SQS Policies
date: 2023-07-20 03:06:00 -700
categories: [Aws-iam,Useful-Policies]
tags: [aws,iam]
---

## SQS Policies
* SQS Read Only Policy:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ListQueues",
                "sqs:ChangeMessageVisibility",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes",
                "sqs:ListQueueTags",
                "sqs:ListDeadLetterSourceQueues",
                "sqs:DeleteMessageBatch",
                "sqs:ChangeMessageVisibilityBatch",
                "sqs:SetQueueAttributes"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:sqs:us-east-1:XXXXXXXXXXXXX:TestQueue"
        }
    ]
}
```
* SQS Write Only Policy:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "sqs:SendMessage"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:sqs:us-east-1:XXXXXXXXXXXXXX:TestQueue"
        }
    ]
}
```