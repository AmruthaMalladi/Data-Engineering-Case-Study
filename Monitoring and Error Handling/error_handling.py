import boto3

def check_failed_ecs_tasks():
    ecs = boto3.client('ecs')
    s3 = boto3.client('s3')

    cluster_name = 'your-ecs-cluster'
    error_archive_bucket = 'advertisex-data'
    error_archive_prefix = 'batch/error_archive/'

    try:
        response = ecs.list_tasks(cluster=cluster_name, desiredStatus='STOPPED', maxResults=10)
        tasks = response['taskArns']

        for task_arn in tasks:
            response = ecs.describe_tasks(cluster=cluster_name, tasks=[task_arn])
            if response['tasks'][0]['lastStatus'] == 'STOPPED' and response['tasks'][0]['stopCode'] != 'EssentialContainerExited':
                failed_task_id = response['tasks'][0]['taskArn'].split('/')[-1]
                # Move partial files to error archive
                move_partial_files_to_error_archive(failed_task_id, error_archive_bucket, error_archive_prefix)
    except Exception as e:
        print(f"Error checking failed ECS tasks: {str(e)}")

def move_partial_files_to_error_archive(task_id, bucket_name, prefix):
    # Move partial files to error archive
    pass

if __name__ == "__main__":
    check_failed_ecs_tasks()
