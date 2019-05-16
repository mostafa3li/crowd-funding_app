from django.shortcuts import render
from users.forms import UserForm,UserProfileInfoForm,UpdateProfile,UserEditForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import UserProfileInfo
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def index(request):
    return render(request,'users/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")





def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            user.save()


            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profilePic' in request.FILES:
                print('found it')
                profile.profilePic = request.FILES['profilePic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'users/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/users/index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'users/login.html', {})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/users/user_login')


# @login_required
# def update_profile(request):
#     args = {}

#     if request.method == 'POST':
#         form = UpdateProfile(request.POST, instance=request.user)
#         form.actual_user = request.user
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('update_profile_success'))
#     else:
#         form = UpdateProfile()

#     args['form'] = form
#     return render(request, 'users/update_profile.html', args)


@login_required
def update_profile(request):
    my_form = UpdateProfile(request.POST or None,instance=request.user)
    
    if my_form.is_valid():
        user = my_form.save()
        customUser= UserProfileInfo.objects.get(user_id=user.id)
        image=customUser.profilePic
        customUser.delete()
        profile_form = UserProfileInfoForm(data=request.POST)
        edit_form = UserEditForm(data=request.POST)
        profile = profile_form.save(commit=False)
        profile.user_id=user.id
        profile.profilePic=image
        edit = edit_form.save(commit=False)
        edit.user = user
        user.save()
        profile.save()
        edit.save()
        return HttpResponse("your data updated succesfully")
    context = {
        'form' : my_form
    }
    return render(request, 'users/update_profile.html',  context)


@login_required
def delete_profile(request):
    user = request.user
    customUser= UserProfileInfo.objects.get(user_id=user.id)
    if request.method == 'POST':
        user.delete()
        customUser.delete()
        return HttpResponse("your account deleted succesfully")
    return render(request, 'users/cancel_user.html', {'user': user,'customUser':customUser})

@login_required
def user_profile(request):
    user = request.user
    customUser= UserProfileInfo.objects.get(user_id=user.id)
    return render(request, 'users/show_user.html', {'user': user,'customUser':customUser})