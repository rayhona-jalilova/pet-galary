# ... (import statements)
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status

from accounts.models import Address

# REGISTER_USER_URL = reverse("accounts:register")
USER_PROFILE = reverse("accounts:profile")
TOKEN_URL = reverse("accounts:login")
LOGOUT_URL = reverse("accounts:logout")
CREATE_USER_URL = reverse("accounts:signup")


def create_user_with_credentials(email, password):
    return get_user_model().objects.create_user(email=email, password=password)


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


class UserPublicAPITests(TestCase):
    """Test cases for authenticating users. Public APIs - Creates a new user."""

    def setUp(self) -> None:
        self.client = APIClient()

    # def test_successful_user_registration(self):
    #     """Test creating a new user using the API."""
    #     # Arrange
    #     payload = {
    #         "first_name": "Test",
    #         "last_name": "Testov",
    #         "phone_number": "+1234457102",
    #         "email": "testing@testing.com",
    #         "password1": "1234test",
    #         "password2": "1234test",
    #     }

    #     # Act
    #     response = self.client.post(CREATE_USER_URL, payload)

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_with_existing_email_returns_error(self):
        """Test returns error if a user with given email exists."""
        # Arrange
        create_user_with_credentials("test@test.com", "1234testing")

        # Act
        payload = {
            "first_name": "Test",
            "last_name": "Testov",
            "phone_number": "+1234457102",
            "email": "test@test.com",
            "password1": "1234testing",
            "password2": "1234testing",
        }
        response = self.client.post(CREATE_USER_URL, payload)

        # Assert
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            "Expected error for existing email",
        )

    def test_password_too_short_returns_error(self):
        """Test returns error if password is too short."""
        # Arrange
        payload = {
            "email": "mytest@gmail.com",
            "first_name": "Test",
            "last_name": "Testov",
            "phone_number": "+12344567102",
            "password1": "1234",
            "password2": "1234",
        }

        # Act
        response = self.client.post(CREATE_USER_URL, payload)

        # Assert
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            "Expected error for short password",
        )

    def test_retrieve_user_unauthorized(self):
        """Test tries to retrieve user data but auth required."""
        # Act
        response = self.client.get(USER_PROFILE)

        # Assert
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
            "Expected unauthorized access",
        )

    def test_create_token_for_user(self):
        """Test generates token for valid credentials."""
        user_details = {
            "email": "test@test.com",
            "first_name": "Test",
            "last_name": "Testov",
            "password": "1234test",
        }

        create_user(**user_details)

        payload = {
            "email": user_details["email"],
            "password": user_details["password"],
        }

        response = self.client.post(TOKEN_URL, payload)

        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AuthorizationTests(TestCase):
    """Set of tests which tests user authorization service."""

    def setUp(self) -> None:
        self.user = create_user_with_credentials(
            email="testing@test.com", password="1234test"
        )
        self.token = Token.objects.create(user=self.user)

    def test_user_login_token_auth(self):
        """Test generates token for valid credentials."""
        user_details = {
            "email": "test@test.com",
            "first_name": "Test",
            "last_name": "Testov",
            "password": "1234test",
        }

        create_user(**user_details)

        payload = {
            "email": user_details["email"],
            "password": user_details["password"],
        }

        response = self.client.post(TOKEN_URL, payload)

        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_logout_token_auth(self):
        """Test for testing user logout."""
        response = self.client.post(LOGOUT_URL, {})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
