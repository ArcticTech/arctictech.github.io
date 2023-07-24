## Setup Discourse Server with AWS Lightsail Guide
This is a guide on the proper way to deploy a Discourse Server on AWS Lightsail. See  
Johnny Chivers Youtube video on "Use AWS Lightsail To Create Your Own Discourse Forum Server" for a walkthrough: https://www.youtube.com/watch?v=KNCo56XL-7M

### Objective
By the end of this guide, you should have a fully running Discourse server that is hosted by you and connected to your own domain. Users will be able to signin or signup for your Discourse directly from your domain. For example:
```
https://discourse.yourdomain.com
```

### Prerequisites
In order to do this guide you must have competed all of the following:
1. Registered a domain with Route53 and setup the hosted zones. See "Setup Route53 Guide" on how to do this. Here is our example domain:
```
Domain Name = "https://www.yourdomain.com"
```
2. Created an AWS Lightsail Instance with a Static IP address. Also, make sure that firewall settings are allow ports 22, 80, and 443. See "Lightsail Instance Guide" on how to do this. Here are the configurations of our Lightsail instance:
```
Instance Name = "My-Discourse-Server"
Server Type = "Ubuntu"
Static IP = "192.0.1.0"
Allow Rule 1: SSH TCP 22
Allow Rule 2: HTTP TCP 80
Allow Rule 3: HTTPS TCP 443
```
3. Most importantly: You must have a PRODUCTION Amazon SES associated with your AWS account or else the Discourse Server will not launch. See the section at the end of this guide on how to get a production SES.

All three of the above steps must be completed before beginning this guide.

### Create an "A" record
First, we need to create an "A" record in our domain's hosted zone which will be the path that our users will use to access our Discourse server.
1. Go to Route53 > hosted zones and click on your domain to open up all of the hosted zones.
2. Click create record.
3. Configure the following. The record name can be anything that you want to proceed your root domain, for example: [discourse.yourdomain.com]. The record type we want to be "A" record. Lastly, under values, paste in the static IP address of our Lightsail instance.
```
Record Name = "discourse.yourdomain.com"
Record Type = "A - Record"
Value = "192.0.1.0"
```
4. Leave all other settings as default and click create.

### Create SES Identity
Next, we will need an SES identity and an email address that our Discourse Server will use to allow our users to manage their Discourse accounts such as creating account, verifying account, resetting passwords, etc.
1. In the AWS console, go to SES > Verified Identities, then click Create Identity.
2. Create an identity for your domain. Configure the following and click Create.
```
Identity type = "Domain"
Domain = "yourdomain.com"
```
3. Then go back to Verified Identities and wait until your domain's identity has been verified. Verification process should take only a few minutes. Scroll down to Customer MAIL FROM domain and you should see that the mail from domain is ```webmaster.yourdomain.com```. Under Publish DNS records you should find the following records:
```
MX: webmaster.yourdomain.com 10 feedback-smtp.us-east-1.amazonses.com
TXT: webmaster.yourdomain.com "v=spf1 include:amazonses.com ~all"
```

4. Since your domain is registered with Amazon Route 53, Amazon SES will automatically update your domain’s DNS server with the necessary records. If you go to Route 53 you should see the above records added to your record set.

5. Once your domain has been verified, create a no-reply email address to the identity as well. Click Create Identity, configure the following and click Create.
```
Identity type = "Email address"
Email address = "no-reply@yourdomain.com"
```

### Create SES SMTP Credentials
Next, we need to create the SMTP Credentials for our Discourse Server to assume in order to use our SES email service.
1. In SES, go to Account Dashboard and find the SMTP Settings section.
2. Make a note of the following SMTP configurations, we will need them later:
```
SMTP endpoint = "email-smtp.us-east-1.amazonaws.com"
STARTTLS Port = 25, 587, 2587
```
3. Click on the Create SMTP Credentials button, this will create an IAM User, and you will be able to download the credentials. These are the credentials to use the IAM user to send emails from your SES email service. Make sure to keep this in a SAFE place. This should look like the following example:
```
IAM user name = "ses-smtp-user.20220203-033437"
Access ID = "HAFAI23LDFSJ3209FJS"
Secret Key = "ADFSLJ23ifojru84F2fo30iKg94+jg93uAFSJ"
```

### Download and Install Discourse
Now we can download and install Discourse on to our Lightsail instance.
1. SSH into the instance and run update + upgrade the instance.
```
sudo apt update
sudo apt upgrade -y
```
2. Next, download discourse to /var/discourse with git clone.
```
sudo git clone https://github.com/discourse/discourse_docker.git /var/discourse
```
3. Cd into /var/discourse and run discourse-setup.
```
cd /var/discourse
sudo ./discourse-setup
```

While ```./discoure-setup``` is running, it will ask you for some information.
1. If you don't have docker on your machine, it might prompt to ask you if you want to install docker. Go ahead and type y for yes.
2. Once it reaches the configuration portion, it will ask you for the host hame of your discourse server. This is just the domain record we created:
```
Hostname for your Discourse? discourse.yourdomain.com
```
3. Next, it wants you to configure an admin email address for the server. This should be an secure email address you check regularly.
```
Email address for admin account(s)? myemail@gmail.com
```
4. In the next four steps, it will ask you about the SMTP information. The SMTP server address is the SMTP endpoint, the SMTP port is the STARTTLS Port on 587, the SMTP user name is your SMTP IAM user's Access ID, the SMTP password is your SMTP IAM user's Secret Key, and finally the Notification email address is the no-reply email we setup in SES. See the following example:
```
SMTP server address? email-smtp.us-east-1.amazonaws.com
SMTP port? 587
SMTP user name? HAFAI23LDFSJ3209FJS
SMTP password? ADFSLJ23ifojru84F2fo30iKg94+jg93uAFSJ
Notification email address? no-reply@yourdomain.com
```
5. After putting in all of that information, it will go ahead and build the server. This should take a good five mins.

### Launch your Server
Once it has completed building, wait another minute or so, and then go to your discourse server via the domain:
```
https://discourse.yourdomain.com
```
1. The first screen you should see is a Register New Account screen, click Register.
2. Select the admin email, create a username, and password.
3. You should then get a confirmation email to your email from your Discourse server to create your admin account. Open the email and click verify.
4. Go through the Discourse front end setup steps and you should have a server fully setup.

### Restore From Backup
If you had an existing Discourse server with all your settings and users, you can restore it from backup to your new server.
1. In your new server, go to Settings > Backups
2. Upload the backup .tar.gz file of your old server.
3. Click Restore and now your old server is restored to your new server.

### Note on Production SES
The prerequisites of this guide is getting a production SES on your AWS account. Unfortunately, your Discourse server will NOT work without it. In order to know if you have a production SES, go to SES and if in the top banner it says you are in sandbox, then you do not have it.

To get a production SES, you must cut a ticket to Amazon requesting it. To cut the ticket, in your sandbox SES, click the request upgrade button. This ticket must be extremely detailed on why you need it in order for them to have enough information to approve you. If it is not sufficiently detailed, they will reject your request. Here is a good example request for the Discourse use case:
```
We are cutting this ticket to request a production SES account. Without a production SES, we are unable to send critical system emails to users. We are in the process of launching a Discourse server on AWS for our community. Discourse requires the use of a system email to be able to send out critical emails including account activation emails, sending out password change emails, sending out notifications, and configuration emails to allow users to connect to their Patreon account. These functions are critical for users to interact with the Discourse platform. In addition to these system critical emails, users have the ability to customize their notification settings in the Discourse platform. Users may configure their profile to receive system notifications on posts, topics they're subscribed to, and when users mention them and/or reply to post and/or send a private message. We have already configured Discourse on a Lightsail instance with the AWS SES service to send out these system emails. However, when the system is attempting to use SES it receives this error: "554 Message rejected: Email address is not verified. The following identities failed the check in region" The reason for this is because SES is in sandbox mode and we need a production SES in order for us to be able to use AWS to host our Discourse server.

Emails will only go to members of our community. Members who are on discourse can opt-in and configure their account to receive as much or as little email notifications as they desire. The most important emails such as account verification, email change, accepting permissions changes are opt out. Our Discourse server is handling all of the email processing, Discourse handles the received bounce. We have admins who are dedicated to customer service of our community and are able to handle complaints if they arise. Both users and admins have the ability to turn off user notifications within Discourse.
```

### Conclusion
Now, you should have a fully running Discourse server that is hosted by you and connected to your own domain. You may direct your users to signin or signup for your Discourse from your domain:
```
https://discourse.yourdomain.com
```






