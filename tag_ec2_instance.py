import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
      instanceId = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
      userIdentity = event['detail']['userIdentity']['accountId']
      ec2.create_tags(
        Resources = [
            instanceId
        ],
        Tags = [
            {
                'Key': 'OwnerId',
                'Value': userIdentity
           },    
        ]
      )
