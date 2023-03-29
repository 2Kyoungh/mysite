from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    
    return render(request, 'profile/main.html')

def bloglist(request):
    
    return render(request, 'profile/pythonEx.html')

def myprofile(request):
    
    return render(request, 'profile/myProfile.html')