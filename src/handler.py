import json
import requests
import logging
import boto3
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
################ Main handler #########################
def main(event, context):
    logger.info(f"Testing Event") 
    logger.info(f"{event}")
    return {
        "statusCode": 200,
        "body": "{}".format(event)
    }