# -*- coding: utf-8 -*-
from django.test import TestCase
from .models import User
from .forms import RegisterForm
from django.core.urlresolvers import reverse
from django.test.client import Client
from .views import user_register


class RegisterTests(TestCase):
    def get_form_data(self, **kwargs):
        data = {
            'username': 'foo',
            'first_name': 'bar',
            'last_name': 'baz',
            'email': 'foo@foo.com',
            'password': '1234567',
            'confirm_password': '1234567'
        }
        data.update(kwargs)
        return data

    class Meta:
        abstract = True


class FormTests(RegisterTests):
    def test_register_form_is_valid(self):
        form = RegisterForm(data=self.get_form_data())
        self.assertEqual(form.is_valid(), True)

    def test_register_form_password_not_equal_confirm(self):
        form = RegisterForm(data=self.get_form_data(confirm_password='not1234567'))
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.errors['__all__'][0], u'Введенные пароли не совпадают')

    def test_register_form_existing_username(self):
        user = User(username='admin', email='foo@bar.com', password='1234567')
        user.save()
        form = RegisterForm(data=self.get_form_data(username='admin'))
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.errors['__all__'][0], u'Пользователь с таким именем уже существует')

    def test_register_form_existing_email(self):
        user = User(username='foo', email='foo@foo.com', password='1234567')
        user.save()
        form = RegisterForm(data=self.get_form_data(username='not_foo'))
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.errors['__all__'][0], u'Пользователь с таким адресом электронной почты уже существует')


class ViewTests(RegisterTests):
    def test_valid_form_user_add(self):
        self.client.post(reverse('user_register'), self.get_form_data())
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get()
        self.assertEqual(user.username, 'foo')

    def test_auth_user_registers_new_as_is(self):
        User.objects.create_user('xxx', '1234567', 'xxx', 'xxx', 'xxx@xxx.com')
        # self.client.post(reverse('user_login'), {'username': 'xxx', 'password': '1234567'})
        self.client.login(username='xxx', password='1234567')
        self.assertIn('_auth_user_id', self.client.session)
        self.client.post(reverse('user_register'), self.get_form_data())
        self.assertEqual(User.objects.count(), 2)

    # def test_auth_user_registers_new_to_be(self):
    #     user = User(username='xxx', password='1234567')
    #     user.save()
    #     self.client.post(reverse('user_login'), {'username': 'foo', 'password': '1234567'})
    #     responce = self.client.post(reverse('user_register'), self.get_form_data())
    #
    #     self.assertEqual(User.objects.count(), 2)







