class HTTPException(Exception):
    def __init__(self, message: str):
        super().__init__(message) 

class HTTPConnectionException(HTTPException):
    def __init__(self, host: str, port: int):
        super().__init__(f'Error while connecting with {host}:{port}') 