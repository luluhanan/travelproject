from django.shortcuts import render
from . models import Place,Customer
# Create your views here.
def home(request):
    obj=Place.objects.all()
    per=Customer.objects.all()
    return render(request,'index.html',{'item':obj,'person':per})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     mul=x*y
#     div=x/y
#     subt=x-y
#     return render(request,'sample.html',{'addition':add,'multiplication':mul,'division':div,'subtraction':subt})
