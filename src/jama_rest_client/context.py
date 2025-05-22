from jama_rest_client.utils.authorization import AuthorizationUtil

class Context:
    host: str
    port: int
    authorization_secret: str

    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.authorization_secret = AuthorizationUtil.getBasicAuthorization(username, password)