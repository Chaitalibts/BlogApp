
from django import forms
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, Loginform ,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group





# Create your views here.

# home
def home(request):
    posts= Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

# post view
def postview(request):
    posts= Post.objects.all()
    return render(request,'blog/postview.html',{'posts':posts})

#about
def about(request):
    return render(request,'blog/about.html')

#contact
def contact(request):
    return render(request,'blog/contact.html')

#dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

#contact
def contact(request):
    return render(request,'blog/contact.html')

#user_logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    

#signup
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'CONGRATULATIONS!!!  you are now AUTHOR')
            user = form.save()
            group = Group.objects.get(name ='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST": 
            form = Loginform(request=request, data =request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successfully !! ')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = Loginform()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


#add post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                messages.success(request,'Your post is Added!!!!')
                title = form.cleaned_data['title']
                category = form.cleaned_data['category']
                desc = form.cleaned_data['desc']
                image = form.cleaned_data['image']
                pst = Post(title=title,desc=desc,category=category,image=image)
                pst.save()
                form = PostForm()
        else:
            form = PostForm() 
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


#update post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                messages.success(request,'Your post is Updated!!!!')
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


#delete post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            messages.success(request,'Your post is Deleted!!!!')
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

