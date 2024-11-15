This project demonstrates the use of Terraform to provision AWS infrastructure components, including SQS Queue, S3 Bucket, Secrets Manager, and an EC2 Instance. After deploying these resources using Terraform, we test them to ensure they are correctly provisioned and functioning. Below are the details for each component:

Step 1: Deploying and Testing SQS Queue
We begin by provisioning an SQS Queue using Terraform. The queue is created using the AWS provider, and its name is passed as a variable. After successfully applying the Terraform configuration, the SQS Queue is verified on the AWS console, ensuring it was created in the correct region. Once the queue is created, we test it by sending and receiving messages using a Python script. The script sends a message with the body "Hello World" to the queue and then receives messages, printing the message ID and message contents to confirm successful operation.

Step 2: Deploying and Testing S3 Bucket
Next, we add an S3 Bucket configuration to the Terraform setup. The S3 bucket is provisioned with the specified name and set to private access. After applying the configuration, we verify the bucket's existence in the AWS console. To test the functionality, we use a Python script to upload a file from the local machine to the S3 bucket and download it back to confirm that the file upload and download operations work correctly.

Step 3: Deploying and Testing Secrets Manager
For managing sensitive data, we utilize AWS Secrets Manager. In this step, we define a secret and store a key-value pair as a version in Secrets Manager using Terraform. After applying the configuration, we verify the secret's existence in the AWS console. To test it, a Python script retrieves the secret from Secrets Manager and prints the stored secret value. This ensures that the secret management system is functioning as expected.

Step 4: Deploying and Testing EC2 Instance
Finally, we provision an EC2 Instance using Terraform. The EC2 instance is configured with a specific AMI ID and instance type (t2.micro). After applying the Terraform configuration, we confirm the instance's existence in the AWS console. The EC2 instance is then tested by obtaining its public IP and connecting to it via SSH using the private key. Once connected, we can access the EC2 instance's terminal and perform further operations or run applications.

Testing and Validation
For each resource, after deploying with Terraform, we conduct tests to verify that the services are functioning as expected:

For SQS, we send and receive messages using the Python boto3 library.
For S3, we upload and download files using the upload_file and download_file methods of the boto3 S3 client.
For Secrets Manager, we retrieve a stored secret using the get_secret_value method of the boto3 Secrets Manager client.
For EC2, we verify SSH access by connecting to the instance via its public IP
