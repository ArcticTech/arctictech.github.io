---
title: Stripe API Guide
date: 2023-07-27 05:00:00 -700
categories: [Aws-lambda,APIs]
tags: [aws,lambda,stripe]
---

## Stripe API Guide
This is a guide on the Stripe API. The Stripe API is a powerful set of tools and endpoints provided by Stripe, a popular online payment processing platform. It allows developers to integrate secure payment processing and various financial functionalities into their web and mobile applications. With the Stripe API, businesses can easily accept credit card payments, handle subscriptions, process refunds, manage customer information, and perform other financial operations programmatically. Stripe's well-documented API enables developers to build seamless and secure payment solutions, providing a streamlined and reliable experience for businesses and their customers.

### Setup the API
1. Go to Stripe, ```https://stripe.com/```, and log in. You must have developer access to the stripe account to do this guide
2. Navigate to the Developers section and click on "API Keys" to obtain your "Publishable" and "Secret" API keys and make a note of these keys.

### Requesting Data
For the detailed documentation check out the documentation link below. Stripe also offers an easy to use CLI to test the API that you can find below. We will use it to make a test request to retrieve a customer's subscription data.
```
Stripe Documentation: https://stripe.com/docs/api/customers/object?lang=curl#customer_object-subscriptions
Stripe CLI: https://stripe.com/docs/stripe-cli
```
1. Use the Stripe CLI to get the customer subscription data. Replace ```sk_live_XXXXXXX``` with your secret key.
```bash
curl https://api.stripe.com/v1/customers/cus_MxAgX7Rvm1CUGK -u sk_live_XXXXXXX -d "expand[]"="subscriptions.data"
```
2. To parse the data, for the product and the customer subscription status, your Python code should look like the following:
```python
product = customer_data['subscriptions']['data'][0]['items']['data'][0]['plan']['product']
active = customer_data['subscriptions']['data'][0]['items']['data'][0]['plan']['active']
```

### Stripe Utility
The following is a simple Stripe Utility in Python that you can use in AWS Lambda to retrieve customer subscription data.
```python
import json
import urllib3
http = urllib3.PoolManager()
#
class StripeUtility:
#
	@classmethod
	def get_customer(self, secret_key, customer_id, **kwargs):
		#Note to get the customer subscriptions: expand='?expand[]=subscriptions.data'
		try:
			method = 'GET'; arguments = ''
			for _ , value in kwargs.items(): arguments += value
			url = 'https://api.stripe.com/v1/customers/' + customer_id + arguments
			headers = urllib3.make_headers(basic_auth=secret_key)
			request = http.request(method, url, headers=headers)
			data = json.loads(request.data)
			if 'error' not in data:
				return {'status': 200, 'message': 'Successfully retrieved data from Stripe.',
						'data': data}
			else:
				return {'status': 400, 'message': 'Error: Stripe returned an error, possibly customer_id does not exist.',
						'data': data}
		except:
			return {'status': 400, 'message': 'Error: Failed to retrieve data from Stripe.',
					'data': None}
```

### Conclusion
Now you have a basic guide on how to set up the Stripe API and use Python to retrieve a customer's subscription data. Remember to keep your Stripe API keys secure and never expose them publicly or in your source code.