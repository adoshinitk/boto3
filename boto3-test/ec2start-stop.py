import boto3

ec2 = boto3.resource("ec2")

regions = []
for region in ec2.meta.client.describe_regions()['Regions']:
    regions.append(region['RegionName'])

    for region in regions:
        ec2 = boto3.resource("ec2",region_name=region)
        print("EC2 Regions: ",region)

#ec2_filter = {'Name':'instance-type','Values':['t2.micro']}
#for i in ec2.instances.filter(Filters=[ec2_filter]):
#    i.stop()