from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from text_to_speech.accounts.models import TextToVoiceUser
from text_to_speech.core.models import IHaveUser

UserModel = get_user_model()


def validate_username(username):
    is_valid = all(ch.isalnum() or ch == '_' for ch in username)

    if not is_valid:
        raise ValidationError("Username must contain only letters, digits, and underscores!")


class Profile(IHaveUser, models.Model):

    MAX_FIRST_NAME_LENGTH = 25
    MAX_LAST_NAME_LENGTH = 25

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    GENDER_CHOICES = [
        ('', 'Not Specified'),
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True)

    # user = models.OneToOneField(
    #     UserModel,
    #     primary_key=True,
    #     on_delete=models.CASCADE,
    # )

    account_balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return str(self.user)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name or self.last_name
