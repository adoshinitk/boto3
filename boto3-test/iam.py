import boto3
iam_username = 'adbto'
policy_arn = 'arn:aws:iam::aws:policy/AmazonS3FullAccess'
iam = boto3.client("iam")

create_user = iam.create_user(UserName=iam_username)
print(f"User {iam_username} created successfully!")
#response = iam.create_login_profile(UserName=new_user_name, Password=password, PasswordResetRequired=True)

attach_policy = iam.attach_user_policy(UserName=iam_username, PolicyArn=policy_arn)
print(f"Policy {policy_arn} attached to user {iam_username} successfully!")

#create policy
import boto3
import json

your_policy_name = 'your_policy_name'

# Replace 'your_policy_document' with the JSON policy document defining the permissions
your_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket-name/*",
                "arn:aws:s3:::your-bucket-name"
            ]
        }
    ]
}
iam = boto3.client('iam')

# Create IAM policy
response = iam.create_policy(
    PolicyName=your_policy_name,
    PolicyDocument=json.dumps(your_policy_document)
)

print(f"IAM policy '{your_policy_name}' created with ARN: {response['Policy']['Arn']}")

'''
import boto3
import argparse #utility for CLI
def create_iam_user(username):
    iam = boto3.client("iam")
    try:
        iam.get_user(UserName=username)
        print(f'User {username} already exists')
    except iam.exceptions.NoSuchEntityException:
        try:
            iam.create_user(UserName=username)
            print(f'User {username} created sucessfully')
        except Exception as e:
            print(f"Error creating {username}: {e}")
username=input("Please enter a IAM user you want to create: ")
create_iam_user(username) 
'''