from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
     if request.method == "POST":
         return render(request, "home.html", {})
     else:
        return render(request, "home.html", {})
    
def fileUpload(request):
    pass
    
    
