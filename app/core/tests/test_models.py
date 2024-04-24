""""Test for models"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests Models"""

    def test_create_user_with_email_success(self):
        """Tests creating user with an email is successful"""
        email = 'test@example.com'
        password = 'testpassw123'
        user = get_user_model().objects.create_user(
            email=email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests if user email is normalized"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_password_hashed(self):
        """Tests if password was hashed correctly"""
        email = 'sample@example.com'
        password = 'sample123'
        user = get_user_model().objects.create_user(email, password)

        self.assertTrue(user.check_password(password))

    def test_create_new_user_without_email(self):
        """Tests if new user has no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'sample123')