import json
import requests
import logging
import boto3

def get_logging() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger

logger = get_logging()

def main(event, context):
    logger.info(f"Testing Event") 
    logger.info(f"{event}")
    print(event)
    return {
        "statusCode": 200,
        "body": "{}".format(event)
    }