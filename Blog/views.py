from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post


# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'Blog/home.html',{'posts':posts})

def about(request):
    return render(request,'Blog/about.html')


def contact(request):
    return render(request,'Blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()

        return render(request,'Blog/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')

def user_signup(request):
    if request.method=="POST":

        form = SignUpForm(request.POST)  
        if form.is_valid():
            
            un=form.cleaned_data['username']
            fn=form.cleaned_data['first_name']
            ln=form.cleaned_data['last_name']
            em=form.cleaned_data['email']
            var=User(username=un,first_name=fn,last_name=ln,email=en)
            var.save()
            #User.objects.create(username=un,first_name=fn,last_name=ln,email=en)
            form = SignUpForm()

    else:
        form= SignUpForm()

    # this form is same as usercreation  but since we wanted to add more fields to the form so we created it seperately in forms.py

    return render(request,'Blog/signup.html',{'form':form})



def user_login(request):

  #first we need to check if the user is lready logged in or not
    if not request.user.is_authenticated: #for that we will be checking by is_authenticated if it is not that means we need to login and perform following actions
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass) # authenticate will check if username=uname and password=pass or not i.e and then stores the object given by them in user variable

                if user is not None:
                    login(request,user) # then we will give the permission to login for the request to the user
                    messages.success(request,'Logged in successfully !')
                    return HttpResponseRedirect('/dashboard/')
                
        else:
            form=LoginForm()
    # if it is loggedin then redirect it to the dashboard

    else:
        return HttpResponseRedirect('/dashboard/')


    
    return render(request,'Blog/login.html',{'form':form})



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')





def add_post(request):
    if request.user.is_authenticated:
        if request.method=="POST":



            form=PostForm(request.POST)  
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
                form=PostForm()

        else:
            form=PostForm()

        return render(request,'Blog/addpost.html',{'form':form})

    else:
        return HttpResponseRedirect('/login/')

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id) #here first get will check if pk and id are equal then it will store the data at that pk in pi object
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()

        else:
            pi = Post.objects.get(pk=id)  
            form = PostForm(instance=pi)

        return render(request,'Blog/updatepost.html',{'form':form})

    else:
        return HttpResponseRedirect('/login/')


def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":  #we have kept delete in post request as it is the safest way to delete data and also we have made the delelte button inside the form with POST request in dashboard.html
            pi=Post.objects.get(pk=id)
            pi.delete()


        return HttpResponseRedirect('/dashboard/')

    else:
        return HttpResponseRedirect('/login/')

