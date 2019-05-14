from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# from django_countries.fields import CountryField
from django.core.validators import RegexValidator
# from taggit.managers import TaggableManager  ##TAGS



######USER######
################

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=0)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    email = models.EmailField(null=True,max_length=50)
    mobile = models.CharField(max_length=11, validators=[RegexValidator(regex='^01[0|1|2|5][0-9]{8}')])
    # Country = CountryField()
    # is_active=models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True,default='profile_pics/nopic.jpeg')

    def __str__(self):
        return self.FirstName