from django.shortcuts import render
from .models import Generaldata
# Create your views here.

def homepage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("rollno")
        detail = request.POST.get("detail")
        data = Generaldata(name = name,roll_no = roll,desc = detail)
        data.save()
    data = Generaldata.objects.all()

    return render(request,"homepage/index.html",{"data":data})