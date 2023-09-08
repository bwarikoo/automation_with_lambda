import json
import boto3

def lambda_handler(event, context):
   s3 = boto3.client('s3')
   sns = boto3.client('sns')
   
   bucket_name = event['detail']['requestParameters']['bucketName']
   
   response = s3.get_bucket_acl(Bucket=bucket_name)
   for grant in response['Grants']:
      if 'URI' in grant['Grantee'] and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
         message = f"S3 bucket '{bucket_name}' has public access."
         sns.publish(
            TopicArn='arn:aws:sns:us-east-1:101986088907:topicname',
            Subject='Action Required! Public S3 Bucket has been created',
            Message=message
         )
         break
   return
