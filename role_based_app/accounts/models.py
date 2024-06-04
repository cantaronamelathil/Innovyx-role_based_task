

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(User):
    USER_ROLES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )
   
    role = models.CharField(max_length=10, choices=USER_ROLES)

    def __str__(self):
        return f"{self.id}:{self.username}"