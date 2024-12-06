from django.db import models
from USERS import signals
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, null=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    upload = models.ImageField(
        upload_to="images/", default="/static/img/default-pfp.jpg", blank=True
    )

    def __str__(self):
        return self.user.username
