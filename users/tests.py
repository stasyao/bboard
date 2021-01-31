from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        user = get_user_model().objects.create_user(
            email='test@mail.com',
            phone_number='1234567890',
            password='testpass123',
        )
        self.assertEqual(user.email, 'test@mail.com')
        self.assertEqual(user.phone_number, '1234567890')

    def test_create_superuser(self):
        superuser = get_user_model().objects.create_superuser(
            email='supertest@mail.com',
            phone_number='0987645321',
            password='supertestpass123',
        )
        self.assertEqual(superuser.email, 'supertest@mail.com')
        self.assertEqual(superuser.phone_number, '0987645321')
