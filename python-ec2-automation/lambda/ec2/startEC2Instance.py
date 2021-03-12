import boto3

#run these programs as lambda functions in AWS

#sample input
#{
#  "instance-ids": "x-xxxxxxxx,x-xxxxxxxx"
#}

def lambda_handler(event, context):
    client = boto3.client('ec2')
    my_list = event['instance-ids'].split(",")
    response = client.start_instances(
        InstanceIds=my_list
        )
    print('Started Instance: '+event['instance-ids'])
    return response['StartingInstances']
