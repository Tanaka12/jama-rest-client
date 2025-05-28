class APIException(Exception):
     def __init__(self, message: str):
        super().__init__(message) 

class APIUnknownException(APIException):
    def __init__(self):
        super().__init__(f'Unknown error while accesing de server') 

class APIUnauthorizedException(APIException):
    def __init__(self):
        super().__init__(f'Error while authenticating with the server')

class APIElementNotFoundException(APIException):
    def __init__(self, resource: str):
        super().__init__(f'Element not found while accessing \'{resource}\'')

