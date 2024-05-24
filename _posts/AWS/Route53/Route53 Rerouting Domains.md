## Route53 Rerouting Domains Guide
This is a guide on rerouting a domain with Route53 on Amazon Web Services. We will reroute a domain using AWS Route 53 and configuring an Amazon S3 bucket to host your static website. By the end of this guide, you'll have a clear understanding of how to set up your domain to point to your S3-hosted website, ensuring that your online presence is not only accessible but also scalable and reliable.

### Prerequisites
In order to do this guide, you will need to already have two domains registered in Route53. See the Route53 Basics Tutorial for more details. We will be using the ```pathfinder.io``` domain we used in that tutorial and also the domain ```pathfinder.net``` domain which we want to route to our main domain.

### Create S3 Bucket
First, we need to create a S3 bucket that will be used to route our domain.
1. Create an S3 bucket and name it ```pathfinder.net```.
2. Make sure to uncheck block all public access.
3. Check the acknowledgement that objects in the bucket might become public, then click create.
4. Then in the bucket properties, under Static Website Hosting, click edit.

### Configuring S3 Static Website Hosting

1. In the Static Website Hosting Section, select Enable.
2. Then for Hosting Type, select Redirect requests for an object.
3. Then in Host Name enter the domain name you want to route to: ```pathfinder.io```.
4. For protocol, select ```https```.

### Creating the Records
Now we need to create the record in our redirect domain ```pathfinder.net``` to point to the S3 endpoint.
1. In Route53, find the hosted zone for your redirect domain and click create record.
2. Select A record for the record type.
3. Select Alias, then in Route Traffic To, select Alias to S3 website endpoint.
4. Select the region that your bucket is in and select the S3 endpoint, then create the record.

Once the record is created, your redirect domain should now redirect to your main domain.

### Result
Now you should have a good understanding of how to reroute domains using AWS Route 53 and S3 buckets. By following the steps outlined, you can easily direct your domain to a static website hosted in an S3 bucket. This approach is cost-effective and offers reliability and scalability for your web presence. With AWS Route 53 and S3, you have the tools to efficiently manage your domains and websites, ensuring accessibility and resilience.

~