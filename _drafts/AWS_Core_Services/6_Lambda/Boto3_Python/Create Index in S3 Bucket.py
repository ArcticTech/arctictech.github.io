import boto3

def getBuckets():
    s3 = boto3.resource("s3")
    print("Buckets Available:")
    for bucket in s3.buckets.all():
        print(bucket.name)
    print("======")
    print(" ")

def createIndexHtml(bucketInput):
    s3 = boto3.resource("s3")
    bucketExist = False
    funcStatus = ""

    for bucket in s3.buckets.all():
        if bucketInput == str(bucket.name):
            bucketExist = True
        else: pass

    if bucketExist == True:
        #Adds index.html to bucket
        with open("index.html", "w") as f:
            f.write("<html><h1>Hello World!</h1></html>")
        with open("index.html", "rb") as f:
            s3.Bucket(bucketInput).put_object(Key="index.html", Body=f)

        #Adds error.html to bucket
        with open("error.html", "w") as f:
            f.write("<html><h1>404 Error! Page does not exist.</h1></html>")
        with open("index.html", "rb") as f:
            s3.Bucket(bucketInput).put_object(Key="error.html", Body=f)

        funcStatus = "Files successfully added."
    else:
        funcStatus = "Bucket does not exist."

    return funcStatus

getBuckets()
bucketName = input("Select Bucket:")
print(createIndexHtml(bucketName))