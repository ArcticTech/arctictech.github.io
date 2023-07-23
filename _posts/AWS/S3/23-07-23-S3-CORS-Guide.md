---
title: S3 CORS Guide
date: 2023-07-23 03:00:00 -700
categories: [Aws-s3]
tags: [aws,s3]
---

## S3 CORS Guide
This is a guide on configuring S3 bucket Cross Origin Resources Sharing (CORS) in Amazon Web Services, allowing one S3 bucket to access the contents of another S3 bucket.

### Objective
Once set up, we should have a good understanding of the process of creating and configuring S3 bucket CORS. You will be able to view a static webpage on one s3 that runs a javascript that is in another s3.

### Prerequisites
Set up two s3 buckets that host static websites. For details on how to setup s3 buckets see "S3 Static Website Guide", ie:

1. Create ```example-mainpage``` bucket and configure it to view static webpages.
2. Create ```example-loadingpage``` bucket and configure it to view static webpages.

### Add Script for Testing
1. For testing CORS, add the following ```index.html``` to your main page bucket. Make sure the link: ```http://example-loadingpage.s3-website-us-east-1.amazonaws.com/loadpage.html``` is the link to your loading page bucket. Replace ```&lt;``` with ```<```.
```html
&lt;html>&lt;body>
&lt;script src="https://code.jquery.com/jquery-1.11.0.min.js">&lt;/script>
&lt;script src="https://code.jquery.com/jquery-migrate-1.2.1.min.js">&lt;/script>
&lt;h1>Welcome to the Main Page!&lt;/h1>
&lt;div id="get-html-from-other-s3">&lt;/div>
&lt;script>
$("#get-html-from-other-s3").load("http://example-loadingpage.s3-website-us-east-1.amazonaws.com/loadpage.html")
&lt;/script>
&lt;/body>
&lt;/html>
```
2. Now add the following ```loadpage.html``` file to your load page bucket:
```html
&lt;html>
&lt;body>
&lt;h2>It worked! We have successfully linked the two buckets.&lt;/h2>
&lt;/body>
&lt;/html>
```

### Configure CORS
Next, configure CORS in your loading page bucket. Under "Properties", expand "Permissions", and click on "Add CORS Configuration". Paste the following permission into the field:
```html
&lt;?xml version="1.0" encoding="UTF-8"?>
&lt;CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    &lt;CORSRule>
       &lt;AllowedOrigin>http://example-mainpage.s3-website-us-east-1.amazonaws.com&lt;/AllowedOrigin>
        &lt;AllowedMethod>GET&lt;/AllowedMethod>
        &lt;MaxAgeSeconds>3000&lt;/MaxAgeSeconds>
        &lt;AllowedHeader>Authorization&lt;/AllowedHeader>
    &lt;/CORSRule>
&lt;/CORSConfiguration>
```
Make sure that the Allowed Origin is the url of your main page, ie: ```http://example-mainpage.s3-website-us-east-1.amazonaws.com```.

### Result
Go to the url to your ```index.html``` on your main page, ie: ```http://example-mainpage.s3-website-us-east-1.amazonaws.com/index.html```. If all is configured, you should see that the linked loading page javascript running.
