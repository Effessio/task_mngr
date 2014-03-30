from django.test import TestCase
from .models import User
from .forms import RegisterForm
from .views import user_register

# __all__ = ['User_']

class UserRegisterTests(TestCase):
    def test_register_form_is_valid(self):
        form_data = {'username': 'foo', 'first_name': 'bar', 'last_name':'baz', 'email': 'foo@foo.com',
                     'password': '1234567', 'confirm_password': '1234567'}
        form = RegisterForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_register_form_password_not_equal_confirm(self):
        form_data = {'username': 'foo', 'first_name': 'bar', 'last_name':'baz', 'email': 'foo@foo.com',
                     'password': '123456', 'confirm_password': '1234567'}
        form = RegisterForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_register_form_existing_username(self):
        user = User(username= 'admin', email= 'foo@bar.com', password= '1234567')
        user.save()
        form_data = {'username': 'admin', 'first_name': 'bar', 'last_name':'baz', 'email': 'foo@foo.com',
                     'password': '1234567', 'confirm_password': '1234567'}
        form = RegisterForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_register_form_existing_email(self):
        user = User(username= 'foo', email='foo@foo.com', password= '1234567')
        user.save()
        form_data = {'username': 'admin', 'first_name': 'bar', 'last_name':'baz', 'email': 'foo@foo.com',
                     'password': '1234567', 'confirm_password': '1234567'}
        form = RegisterForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_valid_form_user_add(self):
        form_data = {'username': 'foo', 'first_name': 'bar', 'last_name':'baz', 'email': 'foo@foo.com',
                     'password': '1234567', 'confirm_password': '1234567'}
        form = RegisterForm(data=form_data)
        response = self.client.post('/users/register/', {'username': 'foo', 'first_name': 'bar', 'last_name':'baz', 'email': 'foo@foo.com',
                     'password': '1234567', 'confirm_password': '1234567'})

        self.assertEqual(User.objects.count(), 1)




