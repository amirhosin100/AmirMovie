from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.user.serializers.user_serializer import (
    UserRegistrationSerializer,
)

user_register_schema = extend_schema(
    request=UserRegistrationSerializer,
    responses={
        400: OpenApiResponse(
            response={
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                    }
                }
            }
        ),
        201: OpenApiResponse(
            response={
                "type": "object",
                "properties": {
                    'refresh': {
                        "type": "string",
                    },
                    'access': {
                        "type": "string",
                    }
                }
            }
        )
    }
)
