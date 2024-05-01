import boto3

def lambda_handler(event, context):
    print("Received event: ", event)  # Log the incoming event structure
    ecs_client = boto3.client('ecs')

    #assuming an S3 event for triggering it. 
    if 'Records' in event and event['Records'][0]['s3']: 
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        print(f"Data uploaded to {bucket_name}/{key} has triggered this function.")

        ecs_client.run_task(
            cluster='yourClusterName',
            launchType='FARGATE',
            taskDefinition='yourTaskDefinitionArn',
            count=1,
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': ['yourSubnetId'],
                    'assignPublicIp': 'ENABLED'
                }
            }
        )
        return {
            'statusCode': 200,
            'body': 'ECS task initiated in response to new data.'
        }
    else:
        return {
            'statusCode': 400,
            'body': 'Event format not recognized.'
        }
