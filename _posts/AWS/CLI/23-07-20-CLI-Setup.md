---
title: AWS CLI Setup
date: 2023-07-20 02:01:00 -700
categories: [Aws-cli]
tags: [aws,aws-cli]
---

## AWS CLI Setup Guide
The AWS Command Line Interface (AWS CLI) is a powerful and versatile tool provided by AWS to interact with AWS services from the command line. It allows users to manage and control their AWS resources, such as EC2 instances, S3 buckets, IAM users, and more, directly from the terminal or command prompt. With the AWS CLI, users can perform a wide range of tasks, including creating and configuring resources, querying data, and automating various processes.

### Install and Configure AWS CLI

1. See this link for install instructions for your os.
```
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

2. For linux, simply use this command:
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

3. Check aws version.
```
aws --version
```

4. Use ```aws configure``` to add your credentials and select your default region:
```
aws configure
```
* Configuration can look as follows
```
AWS Access Key ID: *****
AWS Secret Access Key: *****
Default region name: us-east-1
Default output format:
```

5. You can see your credentials using the following command:
```
cat ~/.aws/credentials
```

Note: In general, using roles is preferred to using credentials, see this [howtogeek.com article on roles vs credentials](https://www.howtogeek.com/devops/iam-users-vs-iam-roles-which-one-should-you-use/) for details. To use roles, refer to the IAM Roles guide.

### Configuring Multiple Profiles
If you work with multiple AWS accounts, you will need to use profiles to manage multiple accounts with the CLI. Check out the following guides for more details:
```
https://stackoverflow.com/questions/44243368/how-to-login-with-aws-cli-using-credentials-profiles
https://dev.to/hmintoh/how-to-use-multiple-aws-accounts-with-the-aws-cli-3lge
```

1. To setup multiple accounts, create/edit the credentials file:
```
vim ~/.aws/credentials
```

2. Add credentials for your profile. Do not use the "profile" prefix.
```
[default]
aws_access_key_id = XXX
aws_secret_access_key = XXX

[helloworld]
aws_access_key_id = XXXX
aws_secret_access_key = XXX
```

3. Edit the region file.
```
vim ~/.aws/config
```

4. Add the profile region, use the "profile" prefix.
```
[default]
region = us-east-1

[profile helloworld]
region = us-east-1
```

5. Verify that the profile is successfully added.
```
aws configure list-profiles
```

### Selecting an AWS Profile

1. Select profile:
```
export AWS_PROFILE=helloworld
```

2. View your current profile.
```
aws configure list
```

### Conclusion
Now you know how to setup your AWS CLI and utilize profiles to manage multiple accounts when needed.