import boto3
import json

policy_name = 'adpolicy1'
with open('policy_document.json', 'r') as file:
    policy_document = json.load(file)
iam = boto3.client('iam')
response = iam.create_policy(
    PolicyName=policy_name,
    PolicyDocument=json.dumps(policy_document),
    Description='policy description'
)

print(f"IAM policy '{policy_name}' created.")
'''
rolename='roletest'
assumerole={
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com",
                "AWS": "arn:aws:iam::560732243518:user/pacu1-User1-GDNQNGYDGX36"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
response = client.create_role(
    RoleName=rolename,
    AssumeRolePolicyDocument=json.dumps(assumerole)
)
'''