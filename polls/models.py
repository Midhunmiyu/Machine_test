from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mob = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    email = models.EmailField()

    def __str__(self):
        return self.name


DURATION_CHOICES = (
    ('4', '4 months'),
    ('6', '6 months'),
)


class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    duration = models.CharField(max_length=1, choices=DURATION_CHOICES, null=True)

    def __str__(self):
        return self.name
