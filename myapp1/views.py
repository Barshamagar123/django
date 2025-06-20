from django.shortcuts import render
from django.http import HttpResponse 
from .models import person
# Create your views here.
def home(request):
    p = person.objects.all()
    # dic = {
    #     'name':"barsha",
    #     'age':22
    # }
    # return HttpResponse("hello world")
    # return render(request,"home.html",dic)
    return render(request,"home.html",{'p':p})


