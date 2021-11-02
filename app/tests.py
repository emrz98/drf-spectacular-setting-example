from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import base64


class TestExample(TestCase):
    def setUp(self) -> None:
        username = "emmanuel"
        password = "1234"
        User.objects.create_user(username=username, password=password)
        credentials = f"{username}:{password}"
        credentials_base64 = base64.b64encode(bytes(credentials, 'utf-8'))
        credential_string = credentials_base64.decode('utf-8')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Basic {credential_string}")

    def create_authentication_tests(self):
        cases = [
            (200, 401),
            ()
        ]

    def test_authentication(self):
        response = self.client.get('/examplate')
        assert response.status_code == 200
        self.client.credentials()
        response = self.client.get('/examplate')
        assert response.status_code == 401