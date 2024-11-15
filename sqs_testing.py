import boto3
sqs = boto3.client('sqs', region_name="ap-south-1") 
s3 = boto3.client('s3', region_name="ap-south-1")

# Initialize Secrets Manager client
secrets_manager = boto3.client('secretsmanager')

queue_url = "https://sqs.ap-south-1.amazonaws.com/010438476172/my_queue1"  

#sending a message
response = sqs.send_message(QueueUrl=queue_url, MessageBody='Hi this is tushar')
print("Message ID:", response.get('MessageId'))

# Receiving a message
messages = sqs.receive_message(QueueUrl=queue_url)
print("Messages:", messages)


## S3 testing

bucket_name = "tusharbt1998"  

# For Uploading the  file
s3.upload_file('/Users/tusharkasana/Downloads/3 fraction decimal.xlsx', bucket_name, 'tusharbt1998')
print("File uploaded successfully")

#secret retrieval
secret = secrets_manager.get_secret_value(SecretId='my_secret1')
print("Secret Value:", secret['SecretString'])

# EC2 Instance ssh connection testing



