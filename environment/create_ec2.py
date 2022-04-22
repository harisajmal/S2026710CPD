#Creation of EC2 instance using boto3  
# Importing boto3 library to make functionality available 
import boto3 

#creating function of name EC2_Instance 
def create_ec2_instance(): 
#try expect exception 
    try: 
        print ("Creating EC2 instance") 
        #creating a resource variable in a method called client and providing the resource name of EC2  
        resource_ec2 = boto3.client("ec2") 
        #running the ec2 instance by providing the parameters 
        resource_ec2.run_instances( 
            ImageId="ami-0c02fb55956c7d316", 
            MinCount=1, 
            MaxCount=1, 
            InstanceType="t2.micro", 
            KeyName="ec2-key-pair" 
        ) 
    except Exception as e: 
        print(e) 
create_ec2_instance() 