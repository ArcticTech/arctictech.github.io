---
title: AWS Overview
date: 2023-07-20 00:01:00 -700
categories: [Aws,Aws-Overview]
tags: [aws]
---

## AWS Overview
Amazon Web Services (AWS) is a cloud computing platform provided by Amazon. It offers a wide range of services, including computing power, storage, databases, analytics, machine learning, and much more. AWS enables businesses to access computing resources on-demand, eliminating the need to invest in costly physical infrastructure and providing a pay-as-you-go model for better cost management.

### How to Use AWS
The best way to understand AWS is to understand some of its uses. Here are four ways common uses of AWS which we find quite common in our work.

1. Static Web Hosting - If you need to host a simple static website, AWS provides a seamless solution. You can store your website content, such as HTML, CSS, images, and JavaScript, in Amazon Simple Storage Service (S3). To ensure easy access for visitors, leverage Amazon Route 53 to host your domain and manage DNS traffic routing. To further enhance website performance, use Amazon CloudFront as a content delivery network (CDN) for fast content distribution, reducing latency and improving user experience across the globe.

![Static_Web_Hosting.png](https://raw.githubusercontent.com/ArcticTech/arctictech.github.io/main/assets/img/posts/Static_Web_Hosting.png?raw=true)

2. Create a CRUD App - Building a CRUD (Create, Read, Update, Delete) application requires a robust infrastructure. AWS offers a plethora of services to facilitate this process. Begin by using Amazon Route 53 for routing traffic to your application. For load balancing, employ Elastic Load Balancing (ELB) to distribute incoming traffic evenly among multiple instances. The application itself can be deployed using Amazon Elastic Container Service (ECS) with container images stored in Amazon Elastic Container Registry (ECR). For the database layer, utilize Amazon Relational Database Service (RDS), which offers managed database solutions supporting various engines like MySQL, PostgreSQL, and more.

![Crud_App.png](https://raw.githubusercontent.com/ArcticTech/arctictech.github.io/main/assets/img/posts/Crud_App.png?raw=true)

3. Create a Data Processing Pipeline - Data processing is a crucial aspect of modern applications, and AWS simplifies this with its powerful services. Start by ingesting data into AWS using Amazon Kinesis Firehose, which collects and loads streaming data directly into Amazon S3 for storage. Process this data using AWS Lambda, a serverless compute service, combined with Amazon Elasticsearch for efficient data analysis. Leverage Kibana, an open-source analytics platform, to visualize and gain insights from the processed data.

![Data_Processing_Pipeline.png](https://raw.githubusercontent.com/ArcticTech/arctictech.github.io/main/assets/img/posts/Data_Processing_Pipeline.png?raw=true)

4. Create a Distributed Serverless Workflow - AWS Lambda enables developers to build serverless workflows that automatically trigger functions based on specific events. In this use case, use Lambda to query an API and write the retrieved data to Amazon DynamoDB, a fully managed NoSQL database. Then, process the data with another Lambda function, and when specific conditions are met, trigger an alert using Amazon Simple Queue Service (SQS) and Amazon Simple Email Service (SES) to notify relevant stakeholders.

![Stock_Prices_App.png](https://raw.githubusercontent.com/ArcticTech/arctictech.github.io/main/assets/img/posts/Stock_Prices_App.png?raw=true)

### Conclusion
AWS is a very powerful tool with a wide array of services to meet diverse needs. From static web hosting to complex data processing pipelines and serverless workflows, AWS offers scalable, reliable, and cost-effective solutions for every stage of application development and deployment. It's worth learning and trying it out.

* Note: the pictures in this post were from a youtube video that did a great job summarizing these AWS use cases, however, I can no longer find the video to give it a proper citation. If someone can find that video, please reach out, I would love to give it credit.

