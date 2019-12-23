from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test cases for admin site"""
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@test.com', name='Michael Super', password='Pass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@test.com', name='User', password='UserPass'
        )

    def test_user_listed(self):
        """Test that users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        resp = self.client.get(url)

        self.assertContains(resp, self.user.name)
        self.assertContains(resp, self.user.email)

    def test_user_change_page(self):
        """Test that the user test page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
