from django.contrib.auth.models import AbstractUser
from django.db import models

class EmailUser(AbstractUser):
    #additional fields here

    def __str__(self):
        return self.email
