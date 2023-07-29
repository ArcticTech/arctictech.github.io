---
title: CloudWatch Billing Alarm Guide
date: 2023-07-23 04:50:00 -700
categories: [Aws-cloudwatch]
tags: [aws,cloudwatch,sns]
---

## CloudWatch Billing Alarm Guide
This is a guide on setting up Billing Alarms using CloudWatch. Billing Alarms warns you when your account goes over a certain threshold. CloudWatch is an AWS service that continuously monitors your AWS account and any services on their performance. After completing this guide check out Lambda SNS Publish to Chime Guide to publish your alerts to messaging applications like Chime, Slack, or Teams.

### Objective
Once set up, we should have a good understanding of the process of setting up billing alarms to keep track of your charges within the AWS cloud. We should be able to receive a notification message once we reach a certain threshold in terms of charges.

### Enable Billing Alerts
To create a billing alarm, you must enable Receive Billing Alerts. Navigate to: Billing Dashboard > Billing Preferences and check Receive Billing Alerts.
```
Receive Billing Alerts = True
```

### Creating the Alarm
Creating billing alarms is under CloudWatch.
1. In the AWS console navigate to Cloudwatch > Billing. Then click "Create Alarm".
2. Under "Specify metric and conditions" click Select Metric.
3. Then select the following: Billing > Total Estimated Charges and select USD EstimatedCharges. Configure the following:
```
Metric Name = "EstimatedCharges"
Currency = "USD"
Statistic = "Maximum"
Period = "6 hours"
Threshold type = "Static"
Condition = "Greater than threshold"
```
4. Then set the amount you want the threshold to be in USD and click Next.
```
Threshold Value (USD) = 25
```
5. In Notification select "In Alarm" for alarm state.
6. For SNS topic, select "Create new topic" then configure the following, then click "Create Topic", and click Next:
```
Create a new topic = "AWS_Billing_Topics"
Email endpoint = "[YOUR EMAIL HERE]"
```

6. Give your alarm a name, add a description, and click Create.
```
Alarm name = "Billing Total >$25
Alarm description = "[YOUR ACCOUNT NAME] Aws account billing total has exceeded $25.00"
```

### Configure Push Notifications
To add a subscriber to this alarm, go to SNS to manage the "Billing_Notifiers" topic.
1. In the AWS console navigate to SNS > Topics.
2. Click on your topic, in our case, it's "Billing_Notifiers".
3. Click "Create Subscription" and add the following to add an SMS notification, then click Create.

### Result
Now you should have your billing alarm set up. To test the SNS simply click on "Billing_Notifiers" and click on "Public Message". For the subject type "Test Message" and in the body type "test". If everything is configured correctly you should receive the notification. After completing this guide check out Lambda SNS Publish to Chime Guide to publish your alerts to messaging applications like Chime, Slack, or Teams.
