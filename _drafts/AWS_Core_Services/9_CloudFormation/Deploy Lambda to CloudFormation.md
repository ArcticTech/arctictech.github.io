## Deploy Lambda to CloudFormation

In this guide we'll use AWS CloudFormation to deploy a Lambda function that will run as our website's canary application. You will need to know how to use AWS Lambda as a prerequisite for this guide.

## Setup Lambda Function

In Lambda, we can create our canary as a lambda function and download the SAM file and deployment package, then upload the deployment package to S3 so that CloudFormation can use it to create our stack.

1. Create a python lambda function with basic execution roles and paste in the code for our canary app:

```
import os
from datetime import datetime
from urllib.request import Request, urlopen

SITE = os.environ['site']  # URL of the site to check, stored in the site environment variable
EXPECTED = os.environ['expected']  # String expected to be on the page, stored in the expected environment variable

def validate(res):
    '''Return False to trigger the canary

    Currently this simply checks whether the EXPECTED string is present.
    However, you could modify this to perform any number of arbitrary
    checks on the contents of SITE.
    '''
    return EXPECTED in res

def lambda_handler(event, context):
    timestamp = str(datetime.now())
    print('Checking {} at {}...'.format(SITE, timestamp))
    try:
        req = Request(SITE, headers={'User-Agent': 'AWS Lambda'})
        if not validate(str(urlopen(req).read())):
            raise Exception('Validation failed')
    except:
        message = 'Check FAILED!'
        print(message)
        return {'status': 400, 'message': message, 'data': timestamp}
    else:
        message = 'Check PASSED!'
        print(message)
        return {'status': 200, 'message': message, 'data': timestamp}
    finally:
        print('Check complete.')
```

2. Add the environmental variables that our code uses for 'site' and 'expected'. In Lambda go to configuration, environment variables and add the following key value pairs. Then save, deploy, and test your lambda.

```
expected = Sign In
site = https://aws.amazon.com/
```

3. Export your function. In Actions > Export your function, click on both "Download the AWS SAM file" and "Download deployment package".

4. Upload your deployment package zip file to S3 so our CloudFormation template can use it to create our stack. You can give it a version number like such: ```v1-canary_awswebsite.zip```. 

## Create a CloudFormation Stack

Now, we'll create a CloudFormation stack in the AWS console using the designer and the code samples provided.

1. Important, now we need to modify the YAML code and add the location of our deployment package which we saved in S3. Grab the S3 uri for our deployment package and copy it. Open up the SAM file we downloaded and past the S3 uri to the YAML code after where it says ```CodeUri:```. The result should look like this:

```
   AWSTemplateFormatVersion: '2010-09-09'
   Transform: 'AWS::Serverless-2016-10-31'
   Description: Canary for checking AWS website
   Resources:
   canaryawswebsite:
    Type: 'AWS::Serverless::Function'
    Properties:
        Handler: lambda_function.lambda_handler
        Runtime: python3.9
        CodeUri: s3://iadss-lite/cf-deployment-packages/canary_awswebsite/v1-canary_awswebsite.zip
        Description: Canary for checking AWS website
        MemorySize: 128
        Timeout: 10
        Role: 'arn:aws:iam::{account_number}:role/Lambda_Admin=sns'
    Environment:
        Variables:
            expected: Sign In
            site: 'https://aws.amazon.com/'
```

2. Now copy the YAML code and we are going to paste it into CloudFormation template designer. Head to the CloudFormation service and click Create Stack. We will use the template designer to create our stack. Select "Create template in Desigh" and click "Create template in Design" to bring up the template designer.

3. In the template designer, click on the Template tab at the bottom and select the YAML option. We want to switch to YAML because the SAM file we downloaded is in YAML. Then paste the YAML code we copied into the code section.

4. Click the refresh button in the designer and you will see that the function is setup. Click the checkmark on the top right of the designer to validate the template. Then, click the button with the cloud-upload icon to create the template.

5. Give the stack a name:

```
prodCanaryAwsWebsite
```

6. Leave the remaining settings as default and click next then submit to create the stack.

Click on the stack to view its progress. Once it flips to ```CREATE_COMPLETE```, we can navigate to Lambda and find that the stack deployed our lambda for us. Test the lambda to make sure it's working properly.

## Updating the Stack

Say you need to update this stack with a new deployment package and a new template, the following is a simple way to do this:

1. Upload your updated deployment package to your s3 bucket. It can be called: ```v2-canary_awswebsite.zip``` and copy the S3 uri.

2. Go to your stack and click Update. Select the "Edit template in designer option" and click "View in Designer" to bring up your template in the code designer.

3. Modify the template, reflect any settings or resources you may have added or changed on your function. Important, make sure to update the location of the code by replacing the old S3 uri in the template with the new S3 uri. Then click through to submit the change.

## Conclusion

Now you know how to use AWS CloudFormation to deploy a Lambda function. If you want to delete the stack, simply select the stack and press delete. Important: note that deleting the stack will delete all the resources it created. It will not delete your deployment package or your templates stored in S3.