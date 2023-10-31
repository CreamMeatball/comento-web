from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def shop(request):
    return render(request, 'pages/shop.html')

def cart(request):
    return render(request, 'pages/cart.html')

def contact(request):
    return render(request, 'pages/contact.html')

def login(request):
    return render(request, 'pages/login.html')

def checkout(request):
    return render(request, 'pages/checkout.html')