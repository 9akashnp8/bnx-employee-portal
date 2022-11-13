from django.test import SimpleTestCase

from employee.models import CustomUser

class TestCustomUserManager(SimpleTestCase):

    databases = '__all__'

    def test_create_user_with_valid_data(self):
        new_user = CustomUser.objects.create_user(
            username='test_username',
            email='test@gmail.com',
            password='test_password'
        )
        print([user for user in CustomUser.objects.all()])
        self.assertEqual(CustomUser.objects.count(), 2) # Why is this user being created after the superuser below?
        self.assertEqual(new_user.email, 'test@gmail.com')

    def test_create_user_with_invalid_data(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(
                username='test_username2',
                email='',
                password='test_password'
            )
    
    def test_create_superuser_with_valid_data(self):
        new_superuser = CustomUser.objects.create_superuser(
            username='test_username3',
            email='test_su@gmail.com',
            password='test_password',
        )
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(new_superuser.email, 'test_su@gmail.com')
        self.assertEqual(new_superuser.is_superuser, True)
        self.assertEqual(new_superuser.is_active, True)
    
    def test_create_superuser_with_invalid_data(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email='test@gmail.com',
                password='test_password',
                is_staff=False
            )
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                email='test2@gmail.com',
                password='test_password',
                is_superuser=False
            )