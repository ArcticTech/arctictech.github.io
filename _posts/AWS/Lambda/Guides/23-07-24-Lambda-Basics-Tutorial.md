---
title: Lambda Basics Tutorial
date: 2023-07-24 09:30:00 -700
categories: [Aws-lambda,Guides]
tags: [aws,lambda,tutorial]
---

## Lambda Basics Tutorial
This is a basics tutorial on AWS Lambda, we'll create a basic lambda function to ping a website to check if the website is down or not. AWS Lambda is a serverless compute service that enables users to run code without managing servers. It automatically scales and manages the underlying infrastructure, allowing developers to focus on writing code to respond to specific events or triggers. Lambda functions are executed in a stateless manner and can be integrated with other AWS services, making it a powerful and efficient solution for building event-driven applications and microservices.

### Objective
Once set up, we should have a good understanding of creating a lambda function and using it to run your code.

### Create a New Lambda Function
1. Go to the AWS Lambda console and click the "Create function" button.
2. Choose "Author from scratch".
3. Enter a name for your function, ie: "canary-example-com".
4. Select "Python 3.10" as the runtime.
5. Architecture, leave as default x86_64.
6. For permissions, if you have already created an existing basic lambda execution role already, then select that role. If not, choose "Create a new role with basic Lambda permissions" and one will be created for you. Note: a basic lambda execution role should have the ```AWSLambdaBasicExecutionRole``` policy attached.
7. Leave everything else as default and click create.

### Writing Code
Now we can write our code directly in the function.

1. In the "Function code" section, replace the existing code with the following Python code. This code uses the python ```urllib``` package to ping ```https://example.com/``` and return the status of the website.
```python
import os
from datetime import datetime
from urllib.request import Request, urlopen
#from slack_utility import SlackBot
#
def canary(site, expected):
	try:
		timestamp = str(datetime.now())
		req = Request(site, headers={'User-Agent': 'AWS Lambda'})
		content = str(urlopen(req).read())
		if expected in content:
			message = 'Successfully pinged {} at {}'.format(site, timestamp)
			return {'status': 200, 'message': message}
		else:
			message = 'CRITICAL ERROR: Received an invalid response from {} at {}'.format(site, timestamp)
			result = {'status': 400, 'message': message}
			#SlackBot.alarm(message, result, channel='critical-errors')
			return result
	except:
		message = 'CRITICAL ERROR: Failed to ping {} at {}'.format(site, str(datetime.now()))
		result = {'status': 400, 'message': message}
		#SlackBot.alarm(message, result, channel='critical-errors')
		return result
#
def lambda_handler(event, context):
	site = 'https://example.com/'
	expected = 'Example Domain'
	result = canary(site, expected)
	return result
```

2. Next, click "Deploy" to deploy your code.

### Test the Lambda Function
Once our code is ready, we can now configure a test event.
1. Click on the dropdown next to the "Test" button and click "Configure test event"
2. For the "Event name," enter any name, ie: "test".
3. For the Event JSON, leave it as default:
```
{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
```
4. Then click save, and your test event is ready.

Important note about events: Events are triggers that initiate the execution of Lambda functions. An event is an external occurrence or action that Lambda listens for and responds to. When an event occurs, it invokes the corresponding Lambda function, allowing the function to execute the code in response to specific actions. These events can have data that is passed to lambda that can be used by our code. In our case the test event is passing the default data shown above in step 3 to our function. However, our code is not actually using this data for anything.

If you ever want to use the event data, within your ```lambda_handler(event, context)``` function you can use the ```event``` variable. For example:
```python
def lambda_handler(event, context):
	print(event)
```

### Invoke the Lambda Function
Now that your function is ready, click test to test the function. If it is all configured correction, you should be able to see the function return:
```
{'status': 200,
 'message': 'Successfully pinged https://example.com/ at <timestamp>'}
```

### Next Steps
Congrats on creating your lambda function this completes our basic lambda tutorial. However, if you'd like to turn this function into a fully working canary, we will need to do the following:
1. We will need to invoke this function with a trigger. To setup a trigger, we can use EventBridge. See the EventBridge Guide for details.
2. We will need an alarm to notify us when the function detects the site is down. To create an alarm see the Slack Webhooks Guide or the SNS Basics Guide for details.

### Conclusion
Now you should have a good understanding of creating and deploying an AWS Lambda function. Whenever you update the code simply click deploy and then test to test the function.