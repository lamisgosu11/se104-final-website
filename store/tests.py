# your test file
from django.test import TestCase


# class to define a test case for login
class UserLoginTestCase(TestCase):

    def setUp(self):
        ...
        
    def tearDown(self):
        ...

    def test_correct_login(self):
        # unit test
        # Corroborate the expected scenario
        ...
    
    def test_if_password_incorrect_then_can_not_login(self):
        # unit test
        # Corroborate that user's password needs to be only the correct one
        ...
    
    def test_if_user_not_registered_can_not_login(self):
        # unit test
        # Corroborate that user's are able to login only if they're registered
    
    ...