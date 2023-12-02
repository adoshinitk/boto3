import boto3

def get_client(service):
    return boto3.client(service)
iam_client = get_client('iam')
s3_client = get_client('s3')

# Get a list of all IAM users
response = iam_client.list_users()
users = response['Users']

def get_users_with_s3_access():
    users_with_s3_access =[]
    for user in users:
        username = user['UserName']
        # Get all attached policies of Users
        user_policies = iam_client.list_attached_user_policies(UserName=username)
        attached_policies = user_policies['AttachedPolicies']

        # Check if the user has the policy for S3 access for Policies Admin access or S3 full access
        for policy in attached_policies:
            if policy['PolicyName'] == 'AmazonS3FullAccess' or 'AdministratorAccess':
                print(f"User {username} has S3 access")
                users_with_s3_access.append(username)

        # Conditon: Check if identity policy  has action S3:ListAllMyBuckets
        else:
            for policy in user_policies.get('AttachedPolicies', []):

                #Get the latest version of policy
                latest_version = iam_client.list_policy_versions(PolicyArn=policy['PolicyArn'])['Versions'][0]['VersionId']

                # Get policy latest version
                policy_document = iam_client.get_policy_version(PolicyArn=policy['PolicyArn'], VersionId=latest_version)['PolicyVersion']['Document']

                # Check if the policy grants s3:ListAllMyBuckets permission
                statements = policy_document.get('Statement', [])

                for statement in statements:
                    if 'Action' in statement and 'Effect' in statement and 'Resource' in statement:
                        actions = statement.get('Action', [])
                        if 's3:ListAllMyBuckets' in actions and 'Effect' in statement and statement['Effect'] == 'Allow' :
                            users_with_s3_access.append(username)

    return users_with_s3_access
users_with_s3_access = get_users_with_s3_access()
print(users_with_s3_access)