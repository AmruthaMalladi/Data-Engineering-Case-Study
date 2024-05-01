import boto3
import datetime

def store_data_to_s3(data, data_type):
    s3 = boto3.client('s3')

    bucket_name = 'advertisex-data'
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    if data_type == 'batch':
        key = f'batch/landing_zone/{current_date}/data.csv'
    elif data_type == 'real_time':
        key = f'real_time/{current_date}/data.json'
    
    try:
        s3.put_object(Bucket=bucket_name, Key=key, Body=data)
        print(f"Data stored successfully to S3: {key}")
    except Exception as e:
        print(f"Error storing data to S3: {str(e)}")

if __name__ == "__main__":
    # Example usage
    data = "Sample data"
    data_type = "batch"  # or "real_time"
    store_data_to_s3(data, data_type)
