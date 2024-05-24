---
title: DDB Policies
date: 2023-07-20 03:05:00 -700
categories: [Aws-iam,Useful-Policies]
tags: [aws,iam]
---

## DDB Policies
* DDB Full Access Limited Tables Policy:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "dynamodb:ListContributorInsights",
                "dynamodb:DescribeReservedCapacityOfferings",
                "dynamodb:ListGlobalTables",
                "dynamodb:ListTables",
                "dynamodb:DescribeReservedCapacity",
                "dynamodb:ListBackups",
                "dynamodb:PurchaseReservedCapacityOfferings",
                "dynamodb:ListImports",
                "dynamodb:DescribeEndpoints",
                "dynamodb:DescribeLimits",
                "dynamodb:ListExports",
                "dynamodb:ListStreams"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeContributorInsights",
                "dynamodb:RestoreTableToPointInTime",
                "dynamodb:UpdateGlobalTable",
                "dynamodb:DeleteTable",
                "dynamodb:UpdateTableReplicaAutoScaling",
                "dynamodb:DescribeTable",
                "dynamodb:PartiQLInsert",
                "dynamodb:GetItem",
                "dynamodb:DescribeContinuousBackups",
                "dynamodb:DescribeExport",
                "dynamodb:EnableKinesisStreamingDestination",
                "dynamodb:BatchGetItem",
                "dynamodb:DisableKinesisStreamingDestination",
                "dynamodb:UpdateTimeToLive",
                "dynamodb:BatchWriteItem",
                "dynamodb:PutItem",
                "dynamodb:PartiQLUpdate",
                "dynamodb:Scan",
                "dynamodb:StartAwsBackupJob",
                "dynamodb:UpdateItem",
                "dynamodb:UpdateGlobalTableSettings",
                "dynamodb:CreateTable",
                "dynamodb:RestoreTableFromAwsBackup",
                "dynamodb:GetShardIterator",
                "dynamodb:ExportTableToPointInTime",
                "dynamodb:DescribeBackup",
                "dynamodb:UpdateTable",
                "dynamodb:GetRecords",
                "dynamodb:DescribeTableReplicaAutoScaling",
                "dynamodb:DescribeImport",
                "dynamodb:DeleteItem",
                "dynamodb:CreateTableReplica",
                "dynamodb:ListTagsOfResource",
                "dynamodb:UpdateContributorInsights",
                "dynamodb:CreateBackup",
                "dynamodb:UpdateContinuousBackups",
                "dynamodb:TagResource",
                "dynamodb:PartiQLSelect",
                "dynamodb:UpdateGlobalTableVersion",
                "dynamodb:CreateGlobalTable",
                "dynamodb:DescribeKinesisStreamingDestination",
                "dynamodb:ImportTable",
                "dynamodb:UntagResource",
                "dynamodb:ConditionCheckItem",
                "dynamodb:Query",
                "dynamodb:DescribeStream",
                "dynamodb:DeleteTableReplica",
                "dynamodb:DescribeTimeToLive",
                "dynamodb:DescribeGlobalTableSettings",
                "dynamodb:DescribeGlobalTable",
                "dynamodb:RestoreTableFromBackup",
                "dynamodb:DeleteBackup",
                "dynamodb:PartiQLDelete"
            ],
            "Resource": [
                "arn:aws:dynamodb:*:116583825520:table/LITE_ProductTable/backup/*",
                "arn:aws:dynamodb:us-east-1:116583825520:table/LITE_ProductTable",
                "arn:aws:dynamodb:*:116583825520:table/LITE_ProductTable/import/*",
                "arn:aws:dynamodb:*:116583825520:table/LITE_ProductTable/index/*",
                "arn:aws:dynamodb:*:116583825520:table/LITE_ProductTable/export/*",
                "arn:aws:dynamodb:*:116583825520:table/LITE_ProductTable/stream/*",
                "arn:aws:dynamodb::116583825520:global-table/LITE_ProductTable"
            ]
        }
    ]
}
```

* DDB Read Write Policy:
```json
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

