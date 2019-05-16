from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=11,
        validators=[RegexValidator('(01)[0-9]{9}',
                                   message="phone number is not valid")])
    profilePic = models.ImageField(upload_to='profilePic', blank=True)

class UserEdit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateTimeField()
    facebook =models.CharField(max_length=500)
    country = models.CharField(max_length=120)

def __str__(self):
    return self.user.username
