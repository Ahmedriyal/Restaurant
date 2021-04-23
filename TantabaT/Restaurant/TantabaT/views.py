from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'html/home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username exist")
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email is already used")
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                user.save()
                auth.login(request, user)

                # if register == 'Employer':
                #     userprofile = UserProfile.objects.create(user=user, is_employer=True)
                #     userprofile.save()
                # else:
                #     userprofile = UserProfile.objects.create(user=user)
                #     userprofile.save()

                messages.info(request, "User created. Login now")
                return redirect('signin')
        else:
            messages.info(request, "Password not matching")
            return redirect('signup')
    else:
        return render(request, 'html/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Wrong username or password")
            return redirect('signin')
    else:
        return render(request, 'html/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')