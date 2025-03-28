import json
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, Response

from src.routers.user_router import user_router_

app = ApiGatewayResolver()

app.include_router(user_router_, prefix='/user')




def lambda_handler(event, context):
    return app.resolve(event, context)
