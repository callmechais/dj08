from django.shortcuts import render
#from .models import

# Create your views here.
def allblogs(request):
    blogs="my blogs"
    return render(request,"blog/allblog.html",{"blogs":blogs})