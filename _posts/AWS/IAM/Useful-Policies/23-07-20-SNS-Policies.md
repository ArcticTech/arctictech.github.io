---
title: SNS Policies
date: 2023-07-20 03:07:00 -700
categories: [Aws-iam,Useful-Policies]
tags: [aws,iam]
---

## SNS Policies
* SNS Read Write Policy:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
              "sns:Publish",
              "sns:Subscribe",
              "sns:CreateTopic",
              "sns:GetTopicAttributes",
              "sns:SetTopicAttributes",
              "sns:TagResource",
              "sns:UntagResource",
              "sns:ListTagsForResource",
              "sns:ListSubscriptionsByTopic"
            ],
            "Resource": [
              "arn:aws:sns:us-east-1::mysnsapp"
            ]
        }
    ]
}
```