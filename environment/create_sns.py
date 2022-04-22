#Creating of SNS Topic Using Boto3  

#Importing the libraries to make the functionality available  

import logging  
import boto3  

from botocore.exceptions import ClientError  

#declaring the reagion  
AWS_REGION = 'us-east-1'  

# logger config 

logger = logging.getLogger()  

logging.basicConfig(level=logging.INFO,  

format='%(asctime)s: %(levelname)s: %(message)s')  

sns_client = boto3.client('sns', region_name=AWS_REGION)  

def create_topic(S2026710Topic):  
    #Creates a SNS notification topic.  
    try:  
        topic = sns_client.create_topic(Name=S2026710Topic)  
        logger.info(f'Created SNS topic {S2026710Topic}.')  
    except ClientError:  
        logger.exception(f'Could not create SNS topic {S2026710Topic}.')  
        raise  
    else:  
        return topic  

if __name__ == '__main__':  

    topic_name = 'S2026710Topic'  
    logger.info(f'Creating SNS topic {topic_name}...')  
    topic = create_topic(topic_name) 