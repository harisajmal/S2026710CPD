#Creating of S3 bucket Using Boto3  

#Importing the libraries to make the functionality available  
import boto3 
from botocore.exceptions import ClientError 
import glob 
import logging
import time 

s3client = boto3.client('s3') 
s3 = boto3.resource('s3') 

#declaring name and region
bucket_name = 's2026710bucket' 
region = 'eu-east-1' 

#code checks whether the bucket with this name already exists or not
def bucketStatus(bucket_name): 
    try: 
        #if bucket exists send message bucket already exists
        response = s3client.head_bucket(Bucket=bucket_name) 
        print('Bucket already exists') 
        return True 
        #error handiling if the access is not allowd to the account
    except ClientError as error: 
        errorCode = int(error.response['Error']['Code']) 
        if errorCode == 403: 
            print ('Bucket is private, access is forbidden to this account') 
            return True 
        elif errorCode == 404: 
            return False 

#if bucket with the name is not existing create bucket with the name specifies
if bucketStatus(bucket_name) is not True: 
    try: 
        bucket = s3.create_bucket(Bucket=bucket_name)    
    except ClientError as error: 
        print(error) 