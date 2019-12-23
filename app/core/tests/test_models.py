from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests (TestCase):
    """Class for defining model test cases"""

    def test_create_user_with_email_succesful(self):
        """Test if user with given email was created"""
        email= 'test@test.com'
        password= 'Pass123'
        name= 'Micahel'

        user = get_user_model().objects.create_user(
            email= email,
            name= name,
            password= password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
