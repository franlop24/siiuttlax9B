from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def fab(request):
    return render(request,'home/fab.html')

