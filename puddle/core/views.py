from django.shortcuts import render, redirect
from items.models import category, item
from .forms import Signupform

def index(request):
    items = item.objects.filter(is_sold=False)[0:9]
    categories = category.objects.all()
    return render(request, "core/index.html", {
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, "core/contact.html")

def Signup(request):
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = Signupform()
    
    return render(request, "core/Signup.html", {
        'form': form
    })

