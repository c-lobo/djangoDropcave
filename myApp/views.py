from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AddRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages

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
            messages.success(request, "Successfully created acount!")
            return redirect("login")
            
    context = {'form': form}
    return render(request, 'myApp/register.html', context=context)

# Login a user
def login(request):
    form = LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
                  
            
    context = {'form2': form}
    return render(request, 'myApp/login.html', context=context)


# dashboard
@login_required(login_url='login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'myApp/dashboard.html', context=context)

# create a record
@login_required(login_url='login')
def create_record(request):
    form = AddRecordForm()
    if request.method == "POST":
        form = AddRecordForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Record was created!")
            return redirect("dashboard")
    context = {'form3': form}
    
    return render(request, 'myApp/create-record.html', context=context)


# update a record
@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated record!")
            return redirect('dashboard')
    
    context = {'form4': form}
    return render(request, 'myApp/update-record.html', context=context)   
    

# view 1 record
@login_required(login_url='login')
def singular_record(request, pk):
    
    all_records = Record.objects.get(id=pk)
    context = {'record': all_records}
    return render(request, 'myApp/view-record.html', context=context)

# delete a record
@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Record has been deleted.")
    return redirect("dashboard")


# user logout
def logout(request):
    
    auth.logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect("login")



