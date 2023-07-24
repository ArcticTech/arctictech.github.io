## Lambda SNS Publish to Chime Guide
This is a guide on using Lambda and SNS to publish messages to Amazon Chime chat room, or to Slack or Microsoft Teams channel via webhooks. This is a great use case for publishing billing alarms to one of these chat applications.

### Objective
Once set up, we should have a good understanding of how to use SNS to trigger a Lambda to post to a webhook.

### Prerequisites
In order do this guide you must have knowledge of how to set up an SNS topic. You can create your own topic or use the example SNS billing topic we created to receive CloudWatch billing alarms called: AWS_Billing_Topics. See Setup CloudWatch Billing Alarm Guide for more details.
```
Name = "AWS_Billing_Topics"
ARN = "arn:aws:sns:us-xxxx-x:XXXXXXXXX:AWS_Billing_Topics"
```

### Lambda Publisher for Chime
1. For Chime, grab the webhook URL for your chime channel. It should look like the following:
```
Chime webhook url: https://hooks.chime.aws/incomingwebhooks/ewiou49-lkfsjd-l23j4-lj2948-our3048?token=XXXXXX
```
See this guide for more details on chime webhooks: https://docs.aws.amazon.com/chime/latest/dg/webhooks.html.

2. Create a lambda function with the following configurations (leaving everything else as default):
```
Author From Scratch = True
Function Name = "AWS_Billing_Publisher"
Runtime = "Python 3.9"
```
3. In the lambda function navigate to Configuration > Environment Variables and add the webhook as an environmental variable.
```
Key = "aws_billing_chime_webhook"
Value = "https://hooks.chime.aws/incomingwebhooks/ewiou49-lkfsjd-l23j4-lj2948-our3048?token=XXXXXX"
```
4. Add the following code to the lambda function:
```
import os
import json
import urllib3
from botocore.exceptions import ClientError
http = urllib3.PoolManager()

def lambda_handler(event, context):

	url = os.environ['aws_billing_chime_webhook']
	message = {"Content": event['Records'][0]['Sns']['Message']}
	encoded_msg = json.dumps(message).encode('utf-8')

	try:
		#=== Run Lambda ===
		response = http.request('POST', url, body=encoded_msg)
		return {'statusCode': 200,'body': json.dumps(message['Content'])}

	except ClientError as error:
		return {'statusCode': 400,'body': error}
```
5. Test the lambda function. Click Test > Configure Test Event > Create new test event. In the dropdown search for SNS Topic Notification and give the event a name and click Create.
```
Event template = "sns-notification"
Event name = "test"
```
6. Click Test to test the function. If successful you should receive a notification in Chime.

### Subscribe Lambda to SNS Topic
Next we need to subscribe our Lambda to our SNS topic. You must have an SNS topic you want to subscribe to already created. We will subscibe our lambda function to the AWS_Billing_Topics that we created in the Setup CloudWatch Billing Alarm Guide.

1. In the lambda function click Add Trigger and configure the following and click Add:
```
Trigger = "SNS"
SNS topic = "arn:aws:sns:us-xxxx-x:XXXXXXXXX:AWS_Billing_Topics"
```

2. To test this out end to end, go to SNS and select the AWS_Billing_Topics and publish a message to the topic. If setup correctly you should be able to receive the message in Chime.

### Lambda Publisher for Slack
For Slack, it's the same steps except with different code and environmental variables.

1. You will need to grab the webhook URL, channel name, and webhook username from Slack. See this guide on how to do this: https://api.slack.com/messaging/webhooks.
2. Add each of these three as environmental variables to your Lambda.
```
Key1 = "aws_billing_slack_webhook"
Value1 = "https://hooks.slack.com/services/xxxxxxx"
Key2 = "aws_billing_channel_name"
Value2 = "#CHANNEL_NAME"
Key3 = "aws_billing_user_name"
Value3 = "WEBHOOK_USERNAME"
```
3. Use the following code for the lambda function:
```
import json
import urllib3
http = urllib3.PoolManager()

def lambda_handler(event, context):
	url = os.environ['aws_billing_slack_webhook']
	msg = {"channel": os.environ['aws_billing_channel_name'],
		"username": os.environ['aws_billing_user_name'],
		"text": event['Records'][0]['Sns']['Message'],
		"icon_emoji": ""}

	encoded_msg = json.dumps(msg).encode('utf-8')
	resp = http.request('POST',url, body=encoded_msg)
	print({"message": event['Records'][0]['Sns']['Message'],
		"status_code": resp.status,
		"response": resp.data})
```

### Lambda Publisher for Microsoft Teams
For Microsoft Teams, it's the same process as well.

1. You will need to grab the webhook URL from Microsoft Teams. See this guide on how to do this: https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using?tabs=cURL#setting-up-a-custom-incoming-webhook.
2. Add each of these three as environmental variables to your Lambda.
```
Key1 = "aws_billing_teams_webhook"
Value1 = "https://outlook.office.com/webhook/xxxxxxx"
```
3. Use the following code for the lambda function:
```
import json
import urllib3
http = urllib3.PoolManager()

def lambda_handler(event, context):
	url = os.environ['aws_billing_teams_webhook']
	msg = {"text": event['Records'][0]['Sns']['Message']}
	encoded_msg = json.dumps(msg).encode('utf-8')
	resp = http.request('POST',url, body=encoded_msg)
	print({
		"message": event['Records'][0]['Sns']['Message'],
		"status_code": resp.status,
		"response": resp.data})
```

### Result
Now you should be able to use SNS to trigger a Lambda to post to a webhook. SNS with Lambda allow you to automatically publish all kinds of notifications and alarms.
