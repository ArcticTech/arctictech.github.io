---
title: IAM Basics Tutorial
date: 2023-07-20 03:00:00 -700
categories: [Aws-iam,Guides]
tags: [aws,iam,tutorial]
---
## IAM Basics Tutorial
This is a basics tutorial on AWS Identity and Access Management (IAM). IAM is a service provided that enables users to securely control access to AWS resources. IAM allows you to create and manage users, groups, and roles with specific permissions, granting fine-grained control over who can perform certain actions on AWS resources. By defining IAM policies, you can ensure that each user or application has precisely the necessary permissions to carry out their tasks, thereby maintaining the security and integrity of your AWS infrastructure. IAM is a fundamental component of AWS security, providing centralized access management to safeguard your cloud resources. allowing you to create Users, Groups, Roles, etc.

### Objective
Once set up, we should have a good understanding of the process of creating Users, Groups, Roles, etc.

### Initial Setup
When you first sign in to AWS you will be signed in as the root user. It is highly recommended to add MFA on your root account. Once you have done this, you should create an IAM admin user that you can use for managing the account instead of using your root account.

### Create individual IAM users
To create an IAM user do the following:
1. Click on Users. Create a user name and check Programmatic access.
2. For permissions go ahead and skip. (we can give permission via groups).
3. Review and Create users.
4. Download csv credentials and keep in a safe and secret place.
*IMPORTANT:* You will never see these credentials again! Also, DO NOT keep these credentials in a folder with git to prevent being pushed to Github!

### Create Groups and Assign Permissions
1. Click Groups. Create a group, for example: "system-admins". 
2. Attach a Policy that you want that group to have. For example: "system-admins" should have the policy permission "SystemAdministrator".
3. Finally, in Groups, under the Users tab, go ahead and add the user you created to your group. Now the user will have all of the permissions of that group.

### Apply Password policy
Go to Account Settings and apply any rules you wish for the passwords your users can set.

### Configure IAM Role
Roles are a very important feature that securely allows one Aws service to talk to another AWS service without the need for managing credentials or having to worry about storing credentials within your virtual machines. We will create a role that allows EC2 full access to S3 here:

1. If you are in the IAM console, click Roles > Create Role. If you are in the EC2 console launching an instance, under Advanced Details, click Create New IAM Profile then Create Role.
2. For Trusted Entity Type select AWS service.
3. For Use Case, select EC2, and click Next.
4. Attach a policy to your role. For our purposes, select the ```AmazonS3FullAccess``` policy and click next.
5. Give the role a name, ie: ```EC2_Admin=S3```.
6. Give the role a description, ie: ```Allows EC2 admin access to S3```.
7. Leave everything else as default and click create role.
8. To use this role, simply go to your EC2 instance and add this role to your instance. Under your EC2 instance, under IAM instance profile, select this role.
9. If properly configured, once you SSH into your instance, you should be able to see the contents of your S3 bucket from your EC2 with the following command:
```
aws s3 ls
```
* Note: See the EC2 Basics Tutorial for details on how to configure an EC2 instance.

### Result
Congrats, now you should have a User, Group, and Roles set up in IAM.


