---
title: SNS Guide
date: 2023-07-29 00:00:00 -700
categories: [Aws-lambda,SNS]
tags: [aws,lambda,sns]
---

## SNS Guide
This guide will go over how to use AWS Simple Notification Service (SNS). SNS is a fully managed pub/sub-messaging service. It enables developers to send messages or notifications to a large number of subscribers, including individuals or multiple endpoints, such as email addresses, SMS messages, mobile push notifications, and HTTP endpoints. SNS provides a highly reliable and scalable solution for broadcasting messages to multiple recipients simultaneously. It simplifies the process of sending notifications and enables event-driven communication between different components of distributed applications. With SNS, developers can easily build flexible and dynamic architectures that react to events and deliver real-time updates to users and systems across various platforms and devices.

### Setup SNS
1. Go to AWS SQS and click on the "Create topic" button to create a new SNS topic.
2. Provide a name and display name for your topic.
3. Click "Create topic" to create your SNS topic.
4. Make sure to make a note of the ARN for the SNS topic that you just created. We will use it next.

### Publish to SNS
Now we can use a Lambda function to publish messages to our SNS topic.

1. Give your lambda role access to SNS. See "IAM Basics Tutorial" on how to use IAM roles.

2. Add this code to your lambda. Make sure to replace the ```AWS_REGION``` with the region you created your SNS topic in.
```python
import logging
import boto3
from botocore.exceptions import ClientError
#
AWS_REGION = 'us-east-1'
#
# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
#
sns_client = boto3.client('sns', region_name=AWS_REGION)
#
def publish_message(topic_arn, message, subject):
    """
    Publishes a message to a topic.
    """
    try:
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject,
        )['MessageId']
    except ClientError:
        logger.exception(f'Could not publish message to the topic.')
        raise
    else:
        return response
```

3. Write a "Hello World" message to your SNS topic. Replace the ```topic_arn``` with the ARN you noted earlier.
```python
def lambda_handler(event, context):
    topic_arn = 'your-topic-ARN'
    message = 'This is a test message on topic.'
    subject = 'This is a message subject on topic.'
    logger.info(f'Publishing message to topic - {topic_arn}...')
    message_id = publish_message(topic_arn, message, subject)
    logger.info(
        f'Message published to topic - {topic_arn} with message Id - {message_id}.'
    )
    return message_id
```

### Verify the Published Message in SNS
1. Go back to the SNS topic.
2. Click on your SNS topic to view its details.
3. Select the "Subscriptions" tab to see the list of subscribers. The published message should be visible in the "Recent deliveries" section.

### Conclusion
Now you have successfully set up a Lambda function to publish messages to an SNS topic. SNS enables you to broadcast messages to multiple subscribers, including email addresses, SMS messages, and more, making it a powerful tool for notifications and communication between different parts of your application. You can now expand this setup to handle different types of messages and customize the delivery options to suit your application's needs. Remember to follow best practices for securing SNS topics and handling messages to ensure reliable message delivery and optimal performance.