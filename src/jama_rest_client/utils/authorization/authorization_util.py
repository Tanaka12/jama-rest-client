import base64

class AuthorizationUtil:
    
    @staticmethod
    def getBasicAuthorization(username: str, password: str):
        token: str = base64.b64encode(f'{username}:{password}'.encode('ascii')).decode('ascii')
        return f'Basic {token}'
