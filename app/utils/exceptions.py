from rest_framework.views import exception_handler
from rest_framework.response import Response
from .custom_exceptions import APIError
from rest_framework.exceptions import ParseError


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if isinstance(exc,ParseError):
        response.data = {"error":True,"msg":"Invalid payload format! please check your payload"}
        return response
    
    if isinstance(exc, APIError):
        return Response(exc.detail,status=exc.status_code)

    if response is not None:
        errors = {}
        for key,value in response.data.items():
            errors[key] = value[0]
        response.data = {"error": True, "errors":errors}
    return response