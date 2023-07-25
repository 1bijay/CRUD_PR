from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .person import Person
from .mydb import insertRecord,selectALL
# Create your views here.
def index(request):
   # return HttpResponse(" Helo from prj_1")
   persons = selectALL()
   print(persons)
   context ={'allperson': persons}
   return render(request, 'prj_1/index.html')
def addnew(request):
    return render(request, 'prj_1/addnew.html')
def savenew(request):
    #receive data  from webfrom and save on database table
    #receive data from webfrom
    pid=request.POST['txt1']
    fullname=request.POST['txt2']
    contactadress=request.POST['txt3']
    print(pid,fullname,contactadress)
    person =(pid,fullname,contactadress)
    insertRecord(person)
    #save on database
    #---
    print("save record successfully")
    return redirect('/'); #redirect to index page