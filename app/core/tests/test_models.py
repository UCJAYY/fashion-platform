"""
This Module contains all test for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


def create_user(email="user@example", password="testpass123"):
    """
    Helper function to create a user.
    """

    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """
    Test the user model.
    """

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful.
        """

        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalized.
        """

        SAMPLE_EMAILS = [["test1@EXAMPLE.com", "test1@example.com"],
                         ["Test2@Example.com", "Test2@example.com"],
                         ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
                         ["test4@example.COM", "test4@example.com"]]

        for email, expected in SAMPLE_EMAILS:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        """
        Test creating user without email raises error.
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_new_superuser(self):
        """
        Test creating a new superuser.
        """

        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
