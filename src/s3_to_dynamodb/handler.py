import json
import requests
import logging
import boto3
import os
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
################ Main handler #########################
def main(event, context):
    dynamo_table = os.getenv('DYNAMODB_TABLE')
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1') 
    table = dynamodb.Table(dynamo_table)
    # Table Data
    table_id = event['id']
    table_date = event['time']
    table_dtype = event['detail-type']
    table_key = event['detail']['object']['key']
    table_size = event['detail']['object']['size']

    #Item Mapping
    item = {
    'id': table_id,
    'date': table_date,
    'detail-type': table_dtype,
    'object_name': table_key,
    'object_size': table_size
    }
    
    print(item)
    print(type(item))
    # Put Item
    table.put_item(Item=item)

    # Item Acknowledge
    print("Data inserted successfully!")
    
    # Step pass

    # Scan the table
    response = table.scan()
    data = response['Items']

    # Check if there's more data to fetch
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    print(data)
    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }