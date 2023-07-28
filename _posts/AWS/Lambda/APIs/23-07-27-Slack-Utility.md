---
title: Slack Utility
date: 2023-07-27 05:05:00 -700
categories: [Aws-lambda,APIs]
tags: [aws,lambda,slack]
---

## Slack Utility
This is the basic Slack utility code.
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
class SlackBot:
#
	@classmethod
	def format_code(self, data):
		return '```'+str(data)+'```'
#
	@classmethod
	def log(self, message, data, channel='test-log'):
#
		if channel == 'test-log':
			webhook_url = 'https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX'
		elif channel == 'customer-log':
			webhook_url = 'https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX'
		elif channel == 'db-sync-log':
			webhook_url = 'https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX'
		elif channel == 'tv0-log':
			webhook_url = 'https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX'
		elif channel == 'tv1-log':
			webhook_url = 'https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX'
		else:
			webhook_url = 'https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX'
#
		text = message + '\n' + self.format_code(data)
		return SlackUtility.post(text, webhook_url)
#
	@classmethod
	def alarm(self, message, data, channel='test-log', dryrun=False):
		bold_message = '*' + message + '*'
#
		if channel == 'test-log':
			alert_message = ':warning: (THIS IS A TEST) ' + message
			webhook_url = 'https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX'
		elif channel == 'critical-errors':
			alert_message = ':warning: *(THIS IS A TEST)* ' + bold_message if dryrun else ':red_siren: ' + bold_message
			webhook_url = 'https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX'
		elif channel == 'user-errors':
			alert_message = ':warning: (THIS IS A TEST) ' + message if dryrun else ':yellow_siren: ' + message
			webhook_url = 'https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX'
		else:
			alert_message = ':warning: (THIS IS A TEST) ' + message
			webhook_url = 'https://hooks.slack.com/services/XXXXXXX/XXXXXXXX/XXXXXXXXXXXXX'
#
		text = alert_message + '\n' + self.format_code(data)
		return SlackUtility.post(text, webhook_url)
```