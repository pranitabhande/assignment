from ast import If
from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from assignment_app.models import Blog, Comment
from assignment_app.serializers import BlogSerializer,CommentSerializer

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    obj=Blog.objects.all()
     
    return render(request,'blog.html',{'blog':obj})

def blog(request,pk):
    obj=Blog.objects.get(id=pk)
    comment=Comment.objects.filter(blog=obj)
    context={'post':obj,'comment':comment}
    print("comment",comment)
    return render(request,'sep_blog.html',context)


def postcommentdata(request):
    if request.method == 'POST':
        data= request.POST.get('comment')
        blogid=request.POST.get('postID')
        blog=Blog.objects.get(id=blogid)
        user=request.user
        
        comment=Comment(data=data,blog=blog,user=user)
        comment.save()
        messages.success(request,'posted successfully')

    return redirect(f'blog/{blogid}')

def submitblog(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            
            title= request.POST.get('title')
            content=request.POST.get('content')
            user=request.user
            
            blog=Blog(title=title,content=content,author=user)
            blog.save()
            messages.success(request,'posted successfully')
            return redirect('home')
        
        return render(request, "submitblog.html")
    else:
        messages.error(request,"login required")
        return redirect('login')

def upvote(request):
    if request.method == 'POST':
        blogid=request.POST.get('postID')
        print("blogid",blogid)
        blog=Blog.objects.get(id=blogid)
        print("blog",blog.upvote)
        blog.upvote = blog.upvote+1
        blog.save()
        print("blog",blog.upvote)
       
        return redirect(f'blog/{blogid}')
    
def downvote(request):
    if request.method == 'POST':
        blogid=request.POST.get('postID')
        
        blog=Blog.objects.get(id=blogid)
        
        blog.downvote = blog.downvote+1
        blog.save()
        
       
        return redirect(f'blog/{blogid}')

def reqlogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.info(request, "Incorrect Credentials")
            return redirect('login')
    
    else:
        return render(request, "login.html")
def reqlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already used")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request, "Password does not match")
            return redirect("register")
    else:
        return render (request, "register.html")


















@api_view(['GET'])
def getdata(request):
    obj=Blog.objects.all()
    ser_obj=BlogSerializer(obj,many=True)

    return Response(ser_obj.data)

@api_view(['POST'])
def postdata(request):
    
    ser_obj=BlogSerializer(data=request.data)
    if ser_obj.is_valid():
        ser_obj.save()

    return Response(ser_obj.data)

@api_view(['PUT'])
def putdata(request,pk):
    obj=Blog.objects.get(id=pk)
    ser_obj=BlogSerializer(instance=obj,data=request.data)
    if ser_obj.is_valid():
        ser_obj.save()

    return Response(ser_obj.data)

