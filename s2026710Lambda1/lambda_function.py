#for label detection

#importing libraries
import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
dynamodb_table = dynamodb.Table('S2026710')
    
def lambda_handler(event, context):
    
    body = json.loads(event["Records"][0]["body"])
    records = json.loads(body["Message"])
    file_name = records["Records"][0]["s3"]["object"]["key"]
    bucket_name = records["Records"][0]["s3"]["bucket"]["name"]
    
    photo= file_name
    bucket= bucket_name

    client=boto3.client('rekognition')
#Detects instances of real-world entities within an image (JPEG or PNG) provided as input
    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
        MaxLabels=5)

    print('Detected labels for ' + photo) 
    
    labels = response.get('Labels', None)
    #the labels detected above found in the images 
    for label in labels:
        dynamodb_table.put_item(Item={
                "image-name": photo,
                "label": label['Name'],
                "conf": Decimal(label['Confidence'])
            })
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))