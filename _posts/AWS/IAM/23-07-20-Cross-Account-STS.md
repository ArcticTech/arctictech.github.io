---
title: Cross Account Write Using STS
date: 2023-07-20 03:01:00 -700
categories: [Aws-iam,Guides]
tags: [aws,iam,tutorial]
---

## Cross Account Write Using STS
This is a guide on setting up cross account access between resources of two AWS accounts using STS. By setting this up we will be able to access particular resources of one account from another account.

### Objective
Once set up, we should have two accounts where a resource from the source account can read, write, access, etc the resources of the destination account.

We will focus on setting up a Lambda function in our source account and having it be able to read / write to a Dynamodb in our destination account for this guide.

### Prerequisites
To do this guide, you will need two AWS accounts with one account being the "SOURCE ACCOUNT" and the other being the "DESTINATION ACCOUNT". You will also need a Dynamodb in your destination account. See Setup Dynamodb guide for more details.

Create a Dynamodb table with the following configurations.
```
Table Name = "wd-ddb-table"
Partition Key = "timestamp"
Sort Key = "uuid"
```

### Setup in Source Account
We first need to create a role and policy inside our Source Account that assumes a role that we will create in our Destination Account.

1. In the Source Account, create an STS policy that our lambda role (which we will create next) will use to access the assumed role in our Destination Account (which we will create later).
```
Name = sts-access-to-<DESTINATION ACCOUNT NUMBER>
```
2. Paste in the following permissions.
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": "arn:aws:iam::<DESTINATION ACCOUNT NUMBER>:role/assume-role-via-<SOURCE ACCOUNT NUMBER>",
            "Effect": "Allow"
        }
    ]
}
```
3. In Source Account, create a new role that our Lambda function (which we will create later) will use. Our Lambda function will use this role to write stuff to our DynamoDB table in our Destination Account. When creating the role make sure to select Lambda for the service use case.
```
Role Name = cross-account-write-to-<DESTINATION ACCOUNT NUMBER>
```

4. In the role, make sure "Edit trust relationship" policy looks like the following.
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```
5. Then, attach the policy we created in the earlier step to this role.
```
Attach Policies = "sts-access-to-<DESTINATION ACCOUNT NUMBER>"
```

### Setup in Destination Account
Now we will create the assumed role our Destination Account and attach the proper permissions.

1. In Destination Account, create the assumed role. For service use case select Lambda.
```
Name = assume-role-via-<SOURCE ACCOUNT NUMBER>
```
2. In the role, edit the trust relationship and change it to the following. This allows the Lambda function (which we will create later) in our source account to access the permissions attached to this role.
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "dynamodb.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringLike": {
          "sts:ExternalId": "arn:aws:lambda:us-west-2:<SOURCE ACCOUNT NUMBER>:function:cross-account-dynamodb-write"
        }
      }
    },
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<SOURCE ACCOUNT NUMBER>:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {}
    }
  ]
}
```
4. Attach the policies of the permissions that you want your Lambda function to use. For purposes of this guide we will attach the AWS managed Dynamodb policy "AmazonDynamoDBFullAccess".
```
Attach Policies = "AmazonDynamoDBFullAccess"
```

### Creating the lambda
Now we can create a Lambda function in our Source Account and attach the ```cross-account-write-to-<DESTINATION ACCOUNT NUMBER>``` role in order to write to the DynamoDB table in our Destination Account.

1. In the Source Account, create a Lambda Function, we will use Python 3.8 as our language. In execution role, select "Use an existing role" and select our cross account write role. Then click "Create".
```
Function Name = "cross-account-dynamodb-write"
Runtime = "Python 3.8"
Use an existing role = "cross-account-write-to-<DESTINATION ACCOUNT NUMBER>"
```
2. In the Lambda function, under Basic settings, change the Timeout to 2 mins to give the function more time to execute.

3. Paste in the following code into our function and click "Save".
```python
import json
import boto3
#
ASSUME_ROLE_ARN = 'arn:aws:iam::<DESTINATION ACCOUNT NUMBER>:role/assume-role-via-<SOURCE ACCOUNT NUMBER>'
#
sts_client = boto3.client('sts', region_name='us-west-2', endpoint_url='https://sts.us-west-2.amazonaws.com')
assumed_role_object=sts_client.assume_role(RoleArn=ASSUME_ROLE_ARN, RoleSessionName='AssumeRoleSession1')
credentials=assumed_role_object['Credentials']
dynamodb=boto3.resource('dynamodb', 'us-west-2',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'])
#
def lambda_handler(event, context):
    table = dynamodb.Table('wd-ddb-table')
    item = {'timestamp': '1970-01-01 00:00:00',
            'uuid' : '00000'}
    table.put_item(Item=item)
    return {'statusCode': 200,'body': json.dumps('Data inserted.')}
```

4. Add a test event (the event does not matter) and click test. If everything is set up correctly you should see your lambda function has successfully written to your DynamoDB table in your destination account.  

### Conclusion
Now you should have two accounts where a Lambda function in the Source Account can read/write the DynamoDB table of your destination account using an assumed role that we set up with STS.
~
