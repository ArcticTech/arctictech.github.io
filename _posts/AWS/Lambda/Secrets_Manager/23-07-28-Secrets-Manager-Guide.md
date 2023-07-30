---
title: Secrets Manager Guide
date: 2023-07-28 08:00:00 -700
categories: [Aws-lambda,Secrets-Manager]
tags: [aws,aws-lambda,secrets-manager]
---

## Secrets Manager Guide
This guide will go over how to use AWS Secrets Manager to manage your keys. Secrets Manager is a service offered that provides a secure and centralized solution for managing sensitive information, such as passwords, API keys, and other credentials. It allows users to store secrets in an encrypted manner, eliminating the need to hardcode them in applications or configuration files. With Secrets Manager, users can easily create, retrieve, and manage secrets through the AWS Management Console or APIs. This service is highly beneficial for maintaining the security and integrity of sensitive data in cloud-based applications, and it integrates seamlessly with other AWS services like Lambda to securely access secrets when needed.

### Setup Secrets Manager
For this guide, we will store our API keys for ChatGPT.
1. Go to ```https://platform.openai.com/account/api-keys``` to grab your ChatGPT Api keys.
2. Go to the AWS Secrets Manager console and click on the "Store a new secret" button.
3. Choose "Other type of secrets" since we're storing an API key.
4. Input the API key in the "Secret key" and "Secret value" fields.
5. Optionally, you can add a description and tags for the secret.
6. Click "Next" and provide a name for your secret.
7. Review the settings and click "Store" to create the secret.
8. Make sure to make a note of the ARN for the secret that you just created. We will use it next.

### Accessing Your Keys
Now we can use the API keys that we stored in the Secrets Manager within our code. Set up a Lambda function and use the following code to access the keys we stored in the secrets manager.

1. Give your lambda role access to Secrets Manager. See "IAM Basics Tutorial" on how to use IAM roles.

2. Add this Secrets Utility code to your lambda function.
```python
import boto3
import json
#
class SecretsUtility:
#
	def __init__(self, secret_arn):
		self.secret_arn = secret_arn
		self.secrets_manager = boto3.client('secretsmanager')
#
	def secret(self):
		try:
			response = self.secrets_manager.get_secret_value(SecretId=self.secret_arn)
			secret_data = json.loads(response['SecretString'])
			return {'status': 200, 'message': 'Successfully retrieved secret.',
					'data': secret_data}
		except:
			return {'status': 400, 'message': 'Error: Failed to retrieved secret.',
					'data': None}
```

3. Use the Secrets Utility to retrieve your API key. Replace the ```secret_arn``` with the secret ARN you noted earlier.
```python
def lambda_handler(event, context):
	secret_arn = 'XXXXXXXXXXXXXXXXXXXXXXX'
	SecretsUtility(secret_arn)
	secret_data = SecretsUtility.secret()
	return secret_data
```

### Conclusion
Now you have successfully created Secrets Manager to store your API key and used a Lambda function with Python to access and use the API key in your application. This ensures that your API key is securely stored and not exposed in your code or configuration files. Remember to follow best practices, such as restricting access to the Lambda function and Secrets Manager, to ensure the security of your sensitive data.