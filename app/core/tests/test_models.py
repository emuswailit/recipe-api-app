from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests (TestCase):

    """Class for defining model test cases"""
    def test_create_user_with_email_succesful(self):
        """Test if user with given email was created"""
        email = 'test@test.com'
        password = 'Pass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalized(self):
        """Tests if email is normalized"""
        email = 'test@TEST.COM'
        password = 'TestPassword123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_valid(self):
        """Check if user email is valid or raise an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                password='Pass123'
            )

    def test_create_superuser_with_email_succesful(self):
        """Tests whether super user was created"""
        user = get_user_model().objects.create_superuser(
            email='test@test.com',
            password='Test123'
        )

        return user

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""

        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)
