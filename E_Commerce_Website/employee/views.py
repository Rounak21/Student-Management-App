from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.contrib.auth.decorators import login_required

# @csrf_exempt
def user_login(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        print("Hey")
        print(type(user))
        if user:
            login(request,user)
            return HttpResponseRedirect(request.GET.get('next'))

        else:
            context['errors']="Please enter Valid Credentials"
            return render(request,'auth/login.html',{'context':context})

    else:
        return render(request,'auth/login.html',{'context':context})

def user_logout(request):
    if request.method=='POST':
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))
    # user=request.user
    # logout(request,user)
    # return render(request, 'auth/logout.html')

def success(request):
    context={}
    print(request.POST)
    print(f"request.POST.get('username) is {request.POST.get('username')}")
    # if request.user != request.POST.get('username'):
    #     context['errors']="username and logged in username does not match"
    #     return render(request,'auth/success.html',context)
    context['user']=request.user
    return render(request,'auth/success.html',context)

# Create your views here.
@login_required(login_url='/login/')
def lists(request):

    context={}
    list_id = []
    employee_lists = User.objects.all()
    print(employee_lists)
    context['employee_lists'] = employee_lists
    return render(request, 'employees/details/list.html', context)


def detail(request, id=None):

    context = {}
    employee= get_object_or_404(User, id=id)
    print(employee) #string representation of Profile
    print(employee.username) #string representation of User model
    print(employee.first_name) 
    context['employee'] = employee
    return render(request, "employees/details/details.html", context)

def add(request):
    context={}
    if request.method == 'POST':
        print(request.POST)
        form_user = UserForm(request.POST)
        user_profile=ProfileForm(request.POST)
        if form_user.is_valid() and user_profile.is_valid():
            new_user=form_user.save()
            new_user.email=request.POST.get('email')
            new_user.save()
            print(type(new_user))
            # new_user.profile.user=User.objects.get(username=form_user.cleaned_data.get('username'))
            new_user.profile.salary=request.POST.get('salary')
            print(type(user_profile.cleaned_data.get('salary')))
            new_user.profile.designation=request.POST.get('designation')
            # print(user_profile)
            new_user.profile.save()
            return HttpResponseRedirect(reverse('employee-list'))
        else:
            print("Burodadubhai")
            return render(request, 'employees/details/add.html', {'form_user':form_user,'user_profile':user_profile})
    else:
        form_user = UserForm()
        user_profile=ProfileForm()
        return render(request, 'employees/details/add.html', {'form_user':form_user,'user_profile':user_profile})

def edit(request, id=None):

    context={}
    user = get_object_or_404(User, id=id)
    profile=get_object_or_404(Profile,user_id=id)
    if request.method == 'POST':
        print(request.POST)
        form_user = UserForm(request.POST,instance=user)
        user_profile=ProfileForm(request.POST,instance=profile)
        print("printing form_usr")
        # print(form_user)
        if form_user.is_valid() and user_profile.is_valid():
            # form_user.save(commit=False)
            user.email=request.POST.get('email')
            print(form_user.cleaned_data.get('password'))
            print(form_user.cleaned_data.get('email'))
            
            user_profile.save()
            form_user.save()
            return HttpResponseRedirect(reverse('employee-list'))
        else:
            return render(request,'employees/details/edit.html', {'form_user':form_user, 'user_profile':user_profile})
    else:
        form_user=UserForm(instance=user)
        user_profile=ProfileForm(instance=profile)
        return render(request, 'employees/details/edit.html', {'form_user':form_user, 'user_profile':user_profile})



    
