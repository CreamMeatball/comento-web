from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')