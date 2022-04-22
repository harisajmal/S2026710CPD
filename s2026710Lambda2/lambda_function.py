#for PE detection

#importing the libraries to make the functionality available
import boto3
import json


def lambda_handler(event, context):
    
    #whenver a lambda functions is trigerd the code will return records of the file image uploaded
    #the record are getting parsed in json
    body = json.loads(event["Records"][0]["body"])
    records = json.loads(body["Message"])  #holds all the message uploaded on s3 
    file_name = records["Records"][0]["s3"]["object"]["key"] #uploading filename
    bucket_name = records["Records"][0]["s3"]["bucket"]["name"] #uploading file to bucket
    
    #file name and bucket and confidence assignment
    photo= file_name
    bucket= bucket_name
    confidence = 70 #all the objects that has a confidence level below 70 will be threshholded
    
    #error handling to make sure the filename and the bucket exists
    if photo and bucket:
        
        #low level client represented amazon rekognition detecting 
        client=boto3.client('rekognition')
        #Detects Personal Protective Equipment (PPE) worn by people detected in an image
        response = client.detect_protective_equipment(Image={'S3Object':{'Bucket':bucket,'Name':photo}}, 
            SummarizationAttributes={'MinConfidence':confidence, 'RequiredEquipmentTypes':['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']})
            
        
        print('Detected PPE for people in image ' + photo) 
        print('\nDetected people\n---------------')   
        
        #all the persons detected in image will be response persons
        #detects PPE worn by up to 15 persons detected in an image.
        for person in response['Persons']:
            
            print('Person ID: ' + str(person['Id']))
            print ('Body Parts\n----------')
            body_parts = person['BodyParts']
            
            #if no body part is detected then the respond will be no body part found
            if len(body_parts) == 0:
                    print ('No body parts found')
            else:
                #all the body parts will be listed
                for body_part in body_parts:
                    print('\t'+ body_part['Name'] + '\n\t\tConfidence: ' + str(body_part['Confidence']))
                    print('\n\t\tDetected PPE\n\t\t------------')
                    ppe_items = body_part['EquipmentDetections']
                    #if the ppe equipment is not detected on body part the system will send the following message
                    if len(ppe_items) ==0:
                        print ('\t\tNo PPE detected on ' + body_part['Name'])
                        sns = boto3.client('sns')
                        number = '+447399871785'
                        response = sns.publish(PhoneNumber = number, Message='no PPE detected' )
                        print(response)
                    else:
                        #all the ppe equipments detected will be listed
                        for ppe_item in ppe_items:
                            print('\t\t' + ppe_item['Type'] + '\n\t\t\tConfidence: ' + str(ppe_item['Confidence'])) 
                            print('\t\tCovers body part: ' + str(ppe_item['CoversBodyPart']['Value']) + '\n\t\t\tConfidence: ' + str(ppe_item['CoversBodyPart']['Confidence']))

                print('-----------')
                