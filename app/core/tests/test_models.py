""""Test for models"""
from decimal import Decimal
from core import models
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests Models"""

    def test_create_user_with_email_success(self):
        """Tests creating user with an email is successful"""
        email='test@example.com'
        password='testpassw123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
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

    def test_create_superuser(self):
        """Test SuperUser."""
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "simple123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """"Test Create Recipe"""
        user = get_user_model().create(
            'test@example.com',
            'testpass123'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Simple recipe name',
            time_minute = '5-10',
            price=Decimal('5.50'),
            description='sample recipe description'
        )

        self.assertEqual(str(recipe), recipe.title)
        # self.assertEqual()