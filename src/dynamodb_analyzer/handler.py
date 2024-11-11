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
    print(json_data)
    print(type(json_data))
    print("prueba")
    json_data_cv = json.loads(json_data['body'])
    print(json_data_cv)
    print("event")
    df_event = pd.DataFrame(json_data_cv)
    print(df_event)
    # Detail Type Staticstics
    dtype_values = df_event['detail-type'].value_counts()
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
