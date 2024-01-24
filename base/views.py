from django.shortcuts import render,redirect
from items.models import Category,Item
from .forms import signupform
from django.contrib.auth import logout

def home(request):
    items=Item.objects.filter(is_sold=False)
    category=Category.objects.all()
    return render(request,'base/home.html',{
        'category':category,
        'items':items
    })


def contact(request):
    return render(request,'base/contact.html')

def signup(request):
    if request.method=="POST":
        form=signupform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')

    form=signupform()
    return render(request,'base/signup.html',context={
        'form':form,
    })
def Logout(request):
    logout(request)
    return redirect('login')