from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def rog(request):
    return render(request,'home/rog.html')

