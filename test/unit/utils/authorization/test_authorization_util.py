from jama_rest_client.utils.authorization import AuthorizationUtil

class TestAuthorizationUtil():

    def test_validate_happy_path_authorization_util_getBasicAuthorization_returns_expected_value(self) -> None:
        authorization = AuthorizationUtil.getBasicAuthorization('DummyUsername', 'DummyPassword')

        expected_authorization: str = 'Basic RHVtbXlVc2VybmFtZTpEdW1teVBhc3N3b3Jk'
        assert expected_authorization == authorization