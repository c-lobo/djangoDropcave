from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

# - homepage
def home(request):
    return render(request, 'myApp/index.html')


# create user
def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            # return redirect("")
            
    context = {'form': form}
    return render(request, 'myApp/register.html', context=context)

def login(request):
    form = LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'myApp/login.html', context=context)

