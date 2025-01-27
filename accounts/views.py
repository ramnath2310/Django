from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect

from django.contrib import messages

# Create your views here.
def register(request):
        if request.method == 'POST':
            
            first_name=request.POST['firstname']
            last_name=request.POST['lastname']
            username = request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
                
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already taken')
                    return redirect('register')
                else:      
                    user=User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request,'Passwords do not match')
                return redirect('register')
        else:
            return render(request,'register.html')
        
def login(request):
     if request.method == 'POST':
          username=request.POST['username']
          password=request.POST['password']   

          user=auth.authenticate(username=username, password=password)

          if user is not None:
               auth.login(request, user)
               return redirect('/')   
          else:
               messages.info(request,'Username or Password is incorrect')
               return redirect('login')
     else:
          return render(request,'login.html')     
def logout(request):
     auth.logout(request)
     return redirect('/')