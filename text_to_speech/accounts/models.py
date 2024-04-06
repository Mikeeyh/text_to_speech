from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models

from django.utils import timezone

from text_to_speech.accounts.managers import TextToVoiceUserManager

"""
Auth in Django:

1. Use built-in user -> works out-of-the-box
2. Use built-in user only for auth and define 'Profile' model for user data
3. Define a custom user model for auth and define 'Profile' model for user data
"""


class TextToVoiceUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):  # 3. Way
    # password -> from 'AbstractBaseUser'
    # last_login -> from 'AbstractBaseUser'

    email = models.EmailField(
        _("email address"),  # we want to use email
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"
    objects = TextToVoiceUserManager()

