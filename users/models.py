from django.db import models
from django.contrib.auth.models import User as UserModel


class User(UserModel):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
