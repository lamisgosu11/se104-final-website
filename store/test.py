# your test file
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from store.models import Customer, Product, Order, OrderItem, ShippingAddress

# class to define a test case for login


class UserLoginTestCase(TestCase):

    def setUp(self):
        ...
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        ...

    def tearDown(self):
        ...
        self.user.delete()
        ...

    def test_correct_login(self):
        # unit test
        # Corroborate the expected scenario
        ...
        self.client.login(username='testuser', password='12345')
        ...

    def test_if_password_incorrect_then_can_not_login(self):
        # unit test
        # Corroborate that user's password needs to be only the correct one
        ...
        self.client.login(username='testuser', password='wrongpassword')
        ...

    def test_if_user_not_registered_can_not_login(self):
        # unit test
        # Corroborate that user's are able to login only if they're registered
        ...
        self.client.login(username='notregistereduser', password='12345')
        ...

# class to define a test case for logout


class UserLogoutTestCase(TestCase):

    def setUp(self):
        ...
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        ...

    def tearDown(self):
        ...
        self.user.delete()
        ...

    def test_logout(self):
        # unit test
        # Corroborate the expected scenario
        ...
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        ...

# class to define a test case for register


class UserRegisterTestCase(TestCase):

    def setUp(self):
        ...
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        ...

    def tearDown(self):
        ...
        self.user.delete()
        ...

    def test_register(self):
        # unit test
        # Corroborate the expected scenario
        ...
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        ...

# class to define a test case for store


class UserStoreTestCase(TestCase):

    def setUp(self):
        ...
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        ...

    def tearDown(self):
        ...
        self.user.delete()
        ...

    def test_store(self):
        # unit test
        # Corroborate the expected scenario
        ...
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        ...


# class to define a test case for cart
class UserCartTestCase(TestCase):

    def setUp(self):
        ...
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        ...

    def tearDown(self):
        ...
        self.user.delete()
        ...

    def test_cart(self):
        # unit test
        # Corroborate the expected scenario
        ...
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        ...


# class to define a test case for checkout


class UserCheckoutTestCase(TestCase):

    def setUp(self):
        ...
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        ...

    def tearDown(self):
        ...
        self.user.delete()
        ...

    def test_checkout(self):
        # unit test
        # Corroborate the expected scenario
        ...
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        ...
