#importing the libraries to make the functionality available
import os
import boto3
import time

s3 = boto3.resource('s3')

#getting the path folder
directory_in_str="/home/ec2-user/environment/images"
directory = os.fsencode(directory_in_str)

#iterating over each file in the images folder, if the image is found it will be uploaded to the bucket
for file in os.listdir(directory):
    time.sleep(30)
    filename = os.fsdecode(file)
    if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):

        strg=directory_in_str+'/'+filename
        #interval of 30 seconds between file upload
        #time.sleep(30)
        print(strg)     
        file = open(strg,'rb')
        #declaring the bucket name where files should be uploaded
        object = s3.Object('s2026710bucket',filename)
        object.put(Body=file,ContentType='image/jpeg')

    else:
        continue