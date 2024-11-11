import json
import logging
import boto3
import pandas as pd

def main(event, context):
    # Check if event is a string before parsing
    if isinstance(event, str):
        json_data = json.loads(event)  # Parse string to JSON (dict)
    else:
        json_data = event
    # Normalize JSON data
    df_data = pd.json_normalize(json_data, meta=['id', 'date','detail-type','object_name''object_size'])
    print(df_data)
    # Detail Type Staticstics
    dtype_values = df_data['detail-type'].value_counts()
    print(dtype_values)
    # json response
    values_response = json.dumps(dtype_values.to_dict())
    print(values_response)
    # Mapping Event
    data_response = {'value_counts':values_response}
    print(data_response)
    # Returning Event
    return {
        "statusCode": 200,
        "body": json.dumps(data_response)
    }
