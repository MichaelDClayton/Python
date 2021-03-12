import boto3

#run these programs as lambda functions in AWS

#sample input
#{
#  "instance-ids": "x-xxxxxxxx,x-xxxxxxxx"
#}

def lambda_handler(event, context):
    my_list = event['instance-ids'].split(",")
    client = boto3.client('ec2')
    response = client.stop_instances(InstanceIds=my_list)
    return response;
    
    