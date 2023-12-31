---
title: S3 Static Website Guide
date: 2023-07-23 02:30:00 -700
categories: [Aws-s3]
tags: [aws,s3]
---

## S3 Static Website Guide
This is a guide on setting up S3 buckets on Amazon Web Services and making the bucket host static websites.

### Objective
Once set up, we should have a good understanding of the process of creating and configuring S3 buckets for hosting static websites. 

You will be able to view publicly the index.html webpage in your s3 bucket by clicking on the endpoint url link, ie: ```example-bucket.s3-website-us-east-1.amazonaws.com```

### Creating S3 Buckets
In the console navigate to S3 and click on "Create Bucket". Then give the bucket a unique name. Note that the bucket name is unique across all aws users. Then select your region, ie:
```
Bucket Name = "example-bucket"
Region = "US Standard"
```

### Configuring Static Host
You can setup your bucket to host your static websites on S3 by using static website hosting.

1. Click on your bucket and go to the "Properties" tab
2. Expand "Static Website Hosting" and note the endpoint url:
```
example-bucket.s3-website-us-east-1.amazonaws.com
```
3. Select "Enable website hosting" and set documents:
```
Index Document = "index.html"
Error Document = "error.html"
```

### Create Upload Webpage
1. Create an ```index.html``` with this "Hello World" HTML (replace ```&lt;``` with ```<```).
```html
&lt;html>
&lt;body>
&lt;h1>Hello World&lt;/h1>;
&lt;/body>;
&lt;/html>;
```
2. Create an ```error.html``` with this "Error" HTML (replace ```&lt;``` with ```<```).
```html
&lt;html>
&lt;body>
&lt;h1>404 Error! Page does not exist.&lt;/h1>;
&lt;/body>;
&lt;/html>;
```

### Configure Permissions
Once the files are uploaded, we need to allow public view permissions and add a bucket policy to your bucket.

1. For the bucket and for each file in the bucket, under "Properties", expand "Permissions", and allow everyone "View Permissions".
```
Grantee = "Everyone"; View Permissions = "Selected"
```
2. Click on the bucket, under "Properties", expand "Permissions", and click on "Edit bucket policy". In the popup window paste in this GetObject policy:
```json
{
  "Id": "Policy1489935006196",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1489935004745",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::example-bucket/*",
      "Principal": "*"
    }
  ]
}
```
Note: this policy can also be generated by clicking on the bottom link to "AWS Policy Generator" or via: ```http://awspolicygen.s3.amazonaws.com/policygen.html```.

3. Click save and refresh the page.
4. Lastly, allow the content to be read by your browser. Go to each of your files in your bucket, under "Properties", expand the "Metadata" tab. Add/Change "Content-Type" value to "text/html". If it is not in the dropdown just type it in.
```
Key = "Content-Type"; Value = "text/html"
```

### Result
Now you should be able to index.html in your s3 bucket as a webpage by clicking on the endpoint url link, ie: ```example-bucket.s3-website-us-east-1.amazonaws.com```.
