import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')

    # Describe all Elastic IPs
    response = ec2_client.describe_addresses()

    for address in response['Addresses']:
        allocation_id = address.get('AllocationId')
        instance_id = address.get('InstanceId')

        # Check if the Elastic IP is unassociated
        if not instance_id:
            print(f"Releasing Elastic IP {address['PublicIp']}")
            ec2_client.release_address(AllocationId=allocation_id)
        else:
            print(f"Elastic IP {address['PublicIp']} is associated with instance {instance_id}")

# Trigger this Lambda function periodically (e.g., using CloudWatch Events)
