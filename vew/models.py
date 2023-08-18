from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    dp = models.ImageField(upload_to="photo/",null=True,blank=True)
    address = models.TextField(help_text="line1, city, state , pin_code")

