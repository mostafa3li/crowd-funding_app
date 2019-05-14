from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

class CustomUser(User):
    pass
    phone = models.CharField(
        max_length=11,
        validators=[RegexValidator('(01)[0-9]{9}',
                                   message="phone number is not valid")])
    profilePics = models.ImageField(upload_to='profilePics', blank=True)