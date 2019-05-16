from django import forms
from users.models import UserProfileInfo,UserEdit
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        )


    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('This Email is registered, use another email.')
        return email

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('phone','profilePic')


class UserEditForm(forms.ModelForm):
     class Meta():
        model = UserEdit
        fields = ('birthdate','facebook','country')


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    birthdate = forms.CharField(required=False)
    facebook = forms.CharField(required=False)
    country = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
        
        
    # def clean_email(self):
    #     username = self.cleaned_data.get('username')
    #     email = self.cleaned_data.get('email')

    #     if email and User.objects.filter(email=email).exclude(username=username).count():
    #         raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
    #     return email

    # def save(self, commit=True):
        
    #     def __init__(self, *args, **kwargs):
    #         user = kwargs.pop('user')
    #         super(UpdateProfile, self).__init__(*args, **kwargs)
            
    #     user = super(UpdateProfile, self).save(commit=False)
    #     user.email = user.email

    #     if commit:
    #         user.save()

    #     return user