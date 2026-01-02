from rest_framework.exceptions import APIException


class APIError(APIException):

    def __init__(self, msg,status_code):        
        self.detail = {"error": True, "msg": msg}
        self.status_code=status_code
        # super().__init__(detail=detail, self.status_code=status_code)
