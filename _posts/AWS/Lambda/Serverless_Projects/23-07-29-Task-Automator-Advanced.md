---
title: Advanced Task Automator Project
date: 2023-07-29 08:30:00 -700
categories: [Aws-lambda,Serverless-Projects]
tags: [aws,lambda,dynamodb,sqs,eventbridge,serverless-projects]
---

## Advanced Task Automator Project
This is a guide for building a serverless task automator with a queue. This is similar to the basic Task Automator project except we have added an SQS queue for a more resilient architecture. Here is the code below:
```python
import json
import boto3
import decimal
from datetime import datetime
from boto3.dynamodb.conditions import Key as dynamoKey
#
class DatabaseScanner:
    """Collects raw user metrics from prod databases."""
    def _scan_pagination_wrapper(self, target, **kwargs):
        """Handles scans of data over 1mb. 
        https://stackoverflow.com/a/38619425/."""
        response = target.scan(**kwargs)
        data = []
        if 'Items' in response:
            data.extend(self._replace_decimals(response['Items']))
        while response.get('LastEvaluatedKey'):
            response = target.scan(ExclusiveStartKey=response['LastEvaluatedKey'], **kwargs)
            if 'Items' in response:
                data.extend(self._replace_decimals(response['Items']))
        return data
#
    def _replace_decimals(self, obj):
        """Helper function replaces Decimal() and Binary() objects.
        https://github.com/boto/boto3/issues/369/."""
        if isinstance(obj, list):
            for i in range(len(obj)):
                obj[i] = self._replace_decimals(obj[i])
            return obj
        elif isinstance(obj, dict):
            for k in obj.keys():
                obj[k] = self._replace_decimals(obj[k])
            return obj
        elif isinstance(obj, decimal.Decimal):
            if obj % 1 == 0:
                return int(obj)
            else:
                return float(obj)
        else:
            return obj
#
    def get(self, date, job):
        """Scans for data from a given UTC date to now() in a given table.
        Example params: date = '1970-01-01 00:00:00',
        job = {"application": "hello-world-webapp","table_name": "webapp_user_logs", 
        "region": "us-east-1","assume_role": "None"}"""
        # Parse Params
        start_date_time = int(datetime.strptime(date, '%Y-%m-%d %H:%M:%S').timestamp())
        end_date_time = int(datetime.now().timestamp())
        table_name = job.get('table_name')
        region = job.get('region')
        #assume_role = job.get('assume_role')
        if not (table_name, region):
            return {'job params incorrect'}
#
        # Define Resources and Key
        local_db = boto3.resource('dynamodb', region_name=region)
        table = local_db.Table(table_name)
        fe = dynamoKey('access_timestamp').between(start_date_time, end_date_time)
        return self._scan_pagination_wrapper(table, FilterExpression=fe)
#
class DataProcesser:
    """Processes data into JSON files and push to S3."""
    def __init__(self, database_scanner, bucketname):
        self.database_scanner = database_scanner
        self.s3 = boto3.resource('s3')
        self.s3client = boto3.client('s3')
        self.bucketname = bucketname
#
    def _get_data(self, date, job):
        """Get data using database scanner"""
        return self.database_scanner.get(date, job)
#
    def _process_put(self, date, job):
        """Checks if there was an upload today. 
        If not, then retrieves data, uploads, and puts into S3."""
#
        # Check Application
        application = job.get('application')
        if not application:
            return {'no application name given'}
#
        # Create Timestamp
        nowdt = datetime.now()
        now = [nowdt.strftime('%Y-%m-%d %H:%M:%S') + 'Z',
        f"/year={nowdt.year}/month={nowdt.month}/day={nowdt.day}/",
        int(datetime.now().timestamp())]
#
        # Create object path
        folder = 'usermetrics/application=' + application
        extension = application + '_userlogs_'
        objectpath = f"{folder}{now[1]}{extension}{now[0]}.json"
        objectpath_split = objectpath.split(extension)
        filename = extension + objectpath_split[1]
        prefix = objectpath_split[0]
        ##prefix = 'usermetrics/application=hello-world-webapp/year=2019/month=11/day=9/' #for testing
#
        # Test if we already uploaded a file today
        s3metadata = self.s3client.list_objects(Bucket=self.bucketname, Prefix=prefix)
        if 'Contents' in s3metadata:
            return {'exists - no new data uploaded: s3://' + self.bucketname + '/' + prefix}
#
        # Retrieved and Upload data
        data = self._get_data(date, job)
        if not data or len(data)==0:
            return {'no new data was retrieved'}
        jsonfile = json.dumps({'user_metrics':data}).encode('UTF-8')
        result = self.s3.Object(self.bucketname, objectpath).put(Body=(bytes(jsonfile)))
        return filename + ' uploaded to s3://' + self.bucketname  if result else 'S3 upload error.'
#
    def load(self, job, pastdays=1):
        """Processes metrics data and loads into S3 for 
        the past number of days (default is 1 day) for a given job.
        Example params: pastdays = 1,
        job = {"application":"hello-world-webapp", "table_name":"webapp_user_logs", 
        "region":"us-east-1","assume_role": "None"}"""
#
        getdate = int(datetime.now().timestamp()) - 86400 * int(pastdays)
        strfdate = datetime.fromtimestamp(getdate).strftime('%Y-%m-%d %H:%M:%S')
        return self._process_put(strfdate, job)
#
class SQSmsgCleaner:
    """Cleans up SQS messages to get the body"""
    def __init__(self, message):
        self.body = json.loads(message['Records'][0]['body'])
#
#===Lambda Handler===
def lambda_handler(event, context):
#
    # Register Classes
    database_scanner = DatabaseScanner()
    data_processer = DataProcesser(database_scanner,bucketname='metrics-bucket')
    sqsmsg = SQSmsgCleaner(event).body
#
    # Run Processer
    result = data_processer.load(sqsmsg)
    print(result)
    return {'statusCode': 200,'body': json.dumps(str(result))}
```
