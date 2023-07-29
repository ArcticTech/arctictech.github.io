---
title: SQS Guide
date: 2023-07-28 10:00:00 -700
categories: [Aws-lambda,SQS]
tags: [aws,lambda,sqs]
---

## SQS Guide
This guide will go over how to use AWS Simple Queue Service (SQS). SQS is a fully managed message queuing service that provides a reliable, scalable, and cost-effective way to decouple and distribute messages between various components of distributed applications. SQS allows applications or microservices to communicate asynchronously, enabling different parts of the application to work independently and at their own pace. Messages are stored in queues and can be processed by one or more consumers, ensuring smooth and efficient handling of tasks and preventing message loss. With SQS, developers can build robust, loosely coupled systems that can handle varying workloads, scale easily, and maintain high availability.

### Setup SQS
1. Go to AWS SQS and click on the "Create New Queue" button to create a new queue.
2. Provide a name for your queue and leave the settings as default.
3. Click "Create Queue" to create your SQS queue.
4. Make sure to make a note of the queue URL for the SQS queue that you just created. We will use it next.

### Writing messages to SQS
Now we can use a Lambda function to write messages to our SQS queue.

1. Give your lambda role access to SQS. See "IAM Basics Tutorial" on how to use IAM roles.

2. Add this SQS Utility code to your lambda function.
```python
import json
import boto3

class SqsUtility:

	@classmethod
	def clean(self, event):
		return json.loads(event['Records'][0]['body'])

	@classmethod
	def write(self, message, queue_url):
		sqs = boto3.client('sqs')
		response = sqs.send_message(QueueUrl=queue_url, MessageBody=message)
		if response['ResponseMetadata']['HTTPStatusCode'] == 200:
			return {'status': 200, 'message': 'Successfully delivered message to SQS queue.',
					'data': message}
		else:
			raise Exception('Error: Failed to deliver message to SQS queue.')
```

3. Use the SQS Utility to write a "Hello World" message to your queue. Replace the ```queue_url``` with the URL you noted earlier.
```python
def lambda_handler(event, context):
	queue_url = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
	message = 'Hello World'
	result = SqsUtility.write(message, queue_url)
	return result
```

### Verify your message in SQS
1. Go back to your SQS queue.
2. Click on your SQS queue to view its details.
3. Select the "View/Delete Messages" option from the "Queue Actions" dropdown and you should see the message sent by the Lambda function in the queue.

### Conclusion
Now you have successfully created set up a Lambda to send messages to an SQS queue. This enables you to decouple components of your application, making it more scalable and robust. You can now expand this setup to handle different types of messages and integrate it into various parts of your application architecture as needed. Remember to follow best practices for securing and handling messages in SQS to ensure the smooth operation of your distributed systems.