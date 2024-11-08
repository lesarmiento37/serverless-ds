import json
import requests
import logging
import boto3

def main(event, context):
    print(event)
    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }