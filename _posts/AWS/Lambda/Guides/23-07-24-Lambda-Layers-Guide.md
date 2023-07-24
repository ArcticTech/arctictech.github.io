---
title: Lambda Layers Guide
date: 2023-07-24 11:00:00 -700
categories: [Aws-lambda,Guides]
tags: [aws,lambda,tutorial]
---

## Lambda Layers Guide
This is a guide on installing packages to Lambda with Lambda Layers. AWS Lambda allows you to upload your code and create a lambda function, while Lambda Layers allows you to package libraries and deploy them to Lambda.

### Objective
Once set up, we should have a good understanding of how to use lambda layers and we will be able to import a Python package that we deployed in our lambda function.
```python
import requests
import xlrd
import pandas as pd
import numpy as np
```

### Prerequisites
To do this guide you must know how to set up an EC2 instance. See Setup EC2 Guide for more details. You will also need to create a role that allows EC2 access to an S3 bucket where you will store your packages. See Setup IAM Guide for more details on creating roles. The bucket we created is called:
```
Bucket name = "package-manager-bucket"
```
In addition, you will need to have created an EC2 instance that is an Ubuntu Server 20.04 LTS machine image. The EC2 is configured as follows. Make sure to up the size of the storage to 12 GiB. Make sure you give your instance a role that allows read-write on S3.
```
Amazon Machine Image = "Ubuntu Server 20.04 LTS (HVM)"
Instance Type = "t2.micro"
IAM role = "EC2-S3-package-manager-access"
Volume Size (GiB) = 12
Name = "Package-Install-Machine"
```
Finally, ssh into your Ubuntu EC2 instance and make sure to update it and reboot.
```
sudo apt update
sudo apt full-upgrade
sudo apt-get dist-upgrade
```

### Install the Latest Python and Pip
Make sure the latest Python version is installed on your Ubuntu AMI. Python version 3.x should be installed by default. Make sure to get the latest Python version that matches the runtime of the Python version that you are using in your lambda function. If it already matches your lambda runtime you can skip this section.

1. Check your Python version.
```
python3 --version
```
2. If your Python version is not the latest, do the following:
```
sudo apt install python3.x -y
```
* Note: for amazon Linux use the following.
```
sudo amazon-linux-extras install python3.x
```
3. Then check the location of the installed package:
```
which python3.x
```
4. Then update Python3 parameter to your newly installed version of python.
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.x 1
python3 --version
```
5. Test that your new Python version is working.
```
python3 -c 'import sys; print(sys.executable);'
```
See this post for details: https://unix.stackexchange.com/questions/410579/change-the-python3-default-version-in-ubuntu

6. Update pip.
```
pip3 install --upgrade pip
```
* Note: if you don't have pip3 install it:
```
sudo apt install python3-pip
```
7. Check pip version and list packages.
```
pip3 --version
pip3 list
```

### Setup Package Library
Now we can setup a package library that we will bring into our lambda layer.

1. Install dependencies.
```
sudo apt install zip
sudo apt install awscli
```
2. Make sure you can install the packages via pip3.
```
pip3 install testresources pandas numpy xlrd requests
python3 -c 'import pandas; print(pandas);'
```
3. Create a package path.
```
mkdir -p build/python/lib/python3.x/site-packages
```
4. Use pip3 to install desired packages into site-packages.
```
sudo -H pip3 install testresources pandas numpy xlrd requests -t build/python/lib/python3.x/site-packages/ --upgrade
```
5. Zip the package.
```
cd build
sudo zip -r data-science-basics-package.zip .
```
6. Copy your new zipped package into your s3 bucket.
```
cd build
aws s3 cp data-science-basics-package.zip s3://package-manager-bucket/data-science-basics-package.zip
```

### Implement Lambda Layer
Now we should be able to create our lambda layer and use it with our lambda functions.

1. Go to lambda, in the left panel, click on layers, and then "Create Layer". Configure the layer as follows and hit create.
```
Name = "ds-basics-layer"
Description = "Data science basics package library."
Upload from S3 = True
S3 Link URL = "https://package-manage-bucket.s3-us-west-2.amazonaws.com/data-science-package.zip"
Runtimes = "Python 3.x"
```
2. Create a lambda function.
```
Function Name = "ds-basics-test"
Runtime = "Python 3.x"
Execution Role = "Create a new role with basic Lambda permissions"
```
3.  Attach the layer to your function, in your lambda function, click "Layers" > "Add a Layer". Then configure the following and click "Add".
```
Custom Layers = True
Choose = "ds-basics-layer"
Version = 1
```
4. Now you should be able to these packages in your lambda function. The following is an example of using the requests package.
```python
import json
import logging
import requests
#
def lambda_handler(event, context):
	""" Demonstrates a simple HTTP request from Lambda """
#
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
#
	response = requests.get('https://jsonplaceholder.typicode.com/posts')
	posts = json.loads(response.text) #load data into a dict of objects, posts
	logger.debug('posts is a = {}'.format(type(posts)))
#
	# Get the unique userId, there should only be 1-10
	unique_ids = set()
#
	for post in posts:
		unique_ids.add(post['userId'])
#
	logger.debug('unique_ids = {}'.format(unique_ids))
	return {'statusCode': 200,'body': json.dumps(str(unique_ids))}
```

### Result
Now you should be able to use Lambda Layers to get packages that you can use in lambda. Lambda Layers allow you to package libraries and deploy them to lambda making a whole host of packages available for your language of choice.
