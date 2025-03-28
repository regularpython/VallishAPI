import json


def lambda_handler(event, context):
    print('Hi Vallish')
    print('Latest code')
    print('Hi')
    endpoint = event['path']
    if endpoint == '/get-all-users':
        # Implement your logic
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Processing get-all-users",
                # "location": ip.text.replace("\n", "")
            }),
        }
    elif endpoint == "/get-user-details":
        # Implement your logic
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Processing /get-user-details",
                # "location": ip.text.replace("\n", "")
            }),
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
