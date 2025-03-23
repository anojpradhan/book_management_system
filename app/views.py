from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect


def home(request):
    return render(request,'home.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method== 'POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
    else:
        form= AuthenticationForm()
    return render(request,'login.html',{'form':form})

def register_page(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})
