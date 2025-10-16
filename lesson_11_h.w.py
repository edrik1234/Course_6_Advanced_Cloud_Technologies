import boto3
import json
import logging

def print_all_s3_objects_client(bucket_name):
    """
    Prints the keys of all objects in a specified S3 bucket using the S3 client
    and handles pagination for large buckets.
    """
    s3_client = boto3.client('s3')
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket = bucket_name, Delimiter = '/')

    print(f"Listing objects in bucket {bucket_name}:")
    for page in pages:
        if 'Contents' in page:
            for obj in page['Contents']:
                print(f"{obj['Key']}")
        else:
            print("Bucket is empty or no objects found in this page.")

def lambda_handler(event, context):
    # TODO implement
    # Retrieve the list of existing buckets
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    s3 = boto3.client('s3')
    response = s3.list_buckets() # rest request to s3 api

    # Output the bucket names
    for bucket in response['Buckets']:
        bucket_name = bucket["Name"]
        try:
            print_all_s3_objects_client(bucket_name)
        except Exception as e:
            print(f"error {e}")
            logger.critical(e)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


