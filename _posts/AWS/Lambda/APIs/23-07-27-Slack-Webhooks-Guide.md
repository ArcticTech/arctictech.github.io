---
title: Slack Webhooks Guide
date: 2023-07-27 05:00:00 -700
categories: [Aws-lambda,APIs]
tags: [aws,lambda,slack]
---

## Slack Webhooks Guide
This is a guide on Slack Webhooks and using AWS Lambda to send messages to Slack via the webhook. The Slack webhook is a feature that allows external applications to send messages directly to Slack channels. It provides a unique URL that acts as a bridge between the application and Slack, enabling automated messages, notifications, or data updates to be posted in real-time. Webhooks are a powerful tool for integrating external systems with Slack, facilitating seamless communication and collaboration within teams.

### Setup the Webhook
To setup a webhook simply do the following.
1. Go to the Slack API website: ```https://api.slack.com/apps``` and sign in with your Slack account.
2. Create a new Slack app by clicking on the "Create an App" button.
3. Click "From Scratch" to create an app from scratch.
4. Give your app a name and select the workspace where you want to use the webhook and click create app.
5. Once the app is created, in the left sidebar, click on "Incoming Webhooks" and toggle the switch to activate it.
6. Click on "Add New Webhook to Workspace" to generate a new webhook URL.
7. Select the Channel that you want your app to post messages to, then click Allow.
8. Now you should have the webhook URL created and be able send messages to. It should look like this:
```
https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX
```

### Use the Webhook
To use the webhook, simply load the following code into your Lambda function and post a "Hello World" message to the webhook. Be sure to replace the ```webhook_url``` with your webhook URL. See Lambda Basics Tutorial for instructions on how to set up an AWS Lambda.

```python
import json
import urllib3
#import certifi
#http = urllib3.PoolManager(ca_certs=certifi.where()) #See post: https://stackoverflow.com/a/72878639
http = urllib3.PoolManager() 
#
class SlackUtility:
#
	@classmethod
	def post(self, text, webhook_url):
		request = {'text': text}
		encoded_request = json.dumps(request).encode('utf-8')
		return http.request('POST', webhook_url, body=encoded_request)
#
text = 'Hello World'
webhook_url = https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX
SlackUtility.post(text, webhook_url)
```

### Conclusion
Now you know the basics of setting up and using Slack webhooks with Python to post messages to your Slack channels. Remember to keep your webhook URL secure as it provides access to post messages to your Slack workspace.