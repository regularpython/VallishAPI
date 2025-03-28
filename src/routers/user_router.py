import json
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, Response, Router

user_router_ = Router()


@user_router_.get("/get-all-users")
def get_details():

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Processing get-all-users",
            # "location": ip.text.replace("\n", "")
        })
    }


@user_router_.get("/get-user-details")
def get_user_details():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Processing /get-user-details",
            # "location": ip.text.replace("\n", "")
        })
    }
