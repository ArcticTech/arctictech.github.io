---
title: AWS CLI Update Security Group
date: 2023-07-23 12:00:00 -700
categories: [Aws-cli]
tags: [aws,aws-cli]
---

## AWS CLI Update Security Group
There are times when you need to update your security group IP addresses that you want to allow to access associated EC2 instances, but you don't want to log in to the console. This guide will show you how to update a security group with the CLI.

This guide follows Visa2Learn's excellent guide and script on Github and Youtube.
```
Github: https://github.com/visa2learn/aws-scripts/blob/main/security-group-cli.sh
Youtube: https://www.youtube.com/watch?v=nEhsiDADJyo
```

### Prerequisites
To do this guide you will need the following:
1. Have a security group already configured. For example:
```
Security Group = "My-Security-Group"
Type = "SSH"
Protocol = "TCP"
Port range = 22
Source = "0.0.0.0"
Description = "My-Access"
```
2. Have Aws CLI installed. See Aws CLI Setup Guide for more details.

3. Have JQ installed. See:
```
https://stedolan.github.io/jq/download/
```

### Configure IAM permissions
Attach the following permissions to the IAM user that you are using with your Aws CLI to manage your security groups.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:RevokeSecurityGroupIngress",
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:UpdateSecurityGroupRuleDescriptionsEgress",
                "ec2:CreateTags",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:ModifySecurityGroupRules",
                "ec2:UpdateSecurityGroupRuleDescriptionsIngress"
            ],
            "Resource": [
                "arn:aws:ec2:*:116583825520:security-group/*",
                "arn:aws:ec2:*:116583825520:security-group-rule/*",
                "arn:aws:ec2:*:116583825520:prefix-list/*"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeSecurityGroupRules",
                "ec2:DescribeSecurityGroupReferences",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeStaleSecurityGroups"
            ],
            "Resource": "*"
        }
    ]
}
```

### Configure Script File

1. Now create the script file.
```
touch allowMyIP.sh
chmod 700 allowMyIP.sh
```

2. View your current aws profile.
```
aws configure list
```

2. Add the following to the script file. Replace ```your_profile_here``` with your current aws profile and add the description identifier that you set for your security group for ```partDescription=```. In our case it's ```My-Access```.
```
#!/bin/bash
#
# Load AWS Profile
export AWS_PROFILE=your_profile_here
#
# User description identifier
partDescription="My-Access"
#
# Get your current IP address
myIP=`curl checkip.amazonaws.com 2>/dev/null`
#
# Get the details of the security groups where your (possibly) old IP address is configured
sGroupsMyIp=`aws ec2 describe-security-groups | jq -r --arg partDescription "$partDescription"  '.SecurityGroups[]? as $sg | $sg.IpPermissions[]? as $ipPerm | $ipPerm.IpRanges[]? as $ipRange | {sgId: $sg.GroupId, fromPort: $ipPerm.FromPort, ipProtocol: $ipPerm.IpProtocol, cidrIp: $ipRange.CidrIp, description: $ipRange.Description} | select (.description | try contains($partDescription))'`
#
# Loops through old IP and replace with current IP.
for sGroupId in `echo $sGroupsMyIp | jq '.sgId' | sort | uniq | sed 's:"::g'`
do
  sgRuleDetail=`echo $sGroupsMyIp | jq --arg sGroupId "$sGroupId" 'select(.sgId | contains($sGroupId))'`
  fromPort=`echo $sgRuleDetail | jq '.fromPort'`
  ipProtocol=`echo $sgRuleDetail | jq '.ipProtocol' | sed 's:"::g'`
  cidrIp=`echo $sgRuleDetail | jq '.cidrIp' | sed 's:"::g'`
  #
  # There can be multiple IP allowlisted for same person
  ipCount=`echo $cidrIp | awk '{print NF}'`
  #
  for i in $(seq 1 $ipCount)
  do
    protocol=`echo $ipProtocol | awk '{print $'$i'}'`
    port=`echo $fromPort | awk '{print $'$i'}'`
    cidr=`echo $cidrIp | awk '{print $'$i'}'`
    #
    # Delete existing(old) IP allowlisting
    echo -e "Revoking Inbound rule for Security Group ($sGroupId): Protocol=$protocol, Port=$port, Source=$cidr"
    aws ec2 revoke-security-group-ingress --group-id $sGroupId --protocol $protocol --port $port --cidr $cidr
    #
    # Add current IP allowlisting
    echo -e "Adding Inbound rule for Security Group ($sGroupId): Protocol=$protocol, Port=$port, Source=$myIP/32\n"
    ipVar="IpProtocol=$protocol,FromPort=$port,ToPort=$port,IpRanges=[{CidrIp=$myIP/32,Description=\"$partDescription\"}]"
    aws ec2 authorize-security-group-ingress --group-id $sGroupId --ip-permissions "$ipVar"
  done
done
```

### Use the Script

1. To use this script simple call it with:
```
./allowMyIP.sh
```

2. Type in the security group you want to modify by inputting the description of the security group.
```
Enter Your Security Group rule description: My-Access
```


