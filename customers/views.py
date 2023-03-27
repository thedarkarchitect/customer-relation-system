from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()

    #check if user logged in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        #user authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:#this those an error of type none should be an httpresponse
            login(request, user)
            messages.success(request, "You have logged In successfully! ")
            redirect('home')
        else:
            messages.success(request, "There was an error, Please Try Again...")
            redirect('home')
    else:
        context ={'records': records}
        return render(request, 'home.html', context)
    
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully been registered")
            return redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})