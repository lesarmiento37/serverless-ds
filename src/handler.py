import json
import requests
import logging
import boto3
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
################ Main handler #########################
def main(event, context):
    logger.info(f"Test Leonardo") 
    return {
        "statusCode": 200,
        "body": "Hello, Leonardo!"
    }