from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests (TestCase):

    """Class for defining model test cases"""
    def test_create_user_with_email_succesful(self):
        """Test if user with given email was created"""
        email = 'test@test.com'
        password = 'Pass123'
        name = 'Micahel'

        user = get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalized(self):
        """Tests if email is normalized"""
        email = 'test@TEST.COM'
        name = 'Test User'
        password = 'TestPassword123'

        user = get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_valid(self):
        """Check if user email is valid or raise an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                password='Pass123',
                name='Michael'
            )

    def test_create_superuser_with_email_succesful(self):
        """Tests whether super user was created"""
        user = get_user_model().objects.create_superuser(
            email='test@test.com',
            name='Michael',
            password='Test123'
        )

        return user
