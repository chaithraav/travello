from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . models import review
from .forms import reviewForm

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/travel/book/booking')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
         return render(request,'login.html')

def register(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'username taken')
               return redirect('register')
            elif User.objects.filter(email=email).exists():
               messages.info(request,'email taken')
               return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)     
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching...')
            return redirect('register')
        return redirect('/travel')
    else:
         return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/travel')

def contact(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/travel/book/cancel')
        else:
            messages.info(request,'invalid credentials')
            return redirect('contact')
    else:
        return render(request,'contact.html')

def feedback(request):
    template_name = 'feedback.html'
    form = reviewForm(request.POST or None)


    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for your feedback!!!')

    except Exception as e:
        form = reviewForm()
        messages.warning(request, 'error in saving. Error: {}'.format(e))

    context = {
        'form':form,
    }
    return render(request, template_name, context)
