# coding: utf-8
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, login, password=None):
        if not email:
            raise ValueError(_('User must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            login=login,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, login, password):
        user = self.create_user(email, login, password)
        user.is_admin = False
        user.is_superuser = False
        user.save(using=self._db)
        return user