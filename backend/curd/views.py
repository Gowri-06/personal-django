from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def test(request):
    # return HttpResponse("<h1>KDG<h1>")
    if request.method == "POST":
        name = request.POST.get("name")
        
        a = Employee(name=name).save()
        
        return HttpResponse(a)
    else:
        return render(request,"folder/index.html")
import sys
print(sys.path)
