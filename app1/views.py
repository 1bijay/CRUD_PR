from django.shortcuts import render, redirect
from django.http import HttpResponse
from pkg1 import person
from pkg1 import mydb

def index(request):
    # return HttpResponse("Hello from index of app1")
    persons = mydb.selectAll()
    print(persons)
    context ={'allperson':persons}
    return render(request, 'app1/index.html', context)

def addnew(request):
    # display new form
    return render(request, 'app1/addnew.html')

def savenew(request):
    # receive data from webform and save on database table
    # receive data from webform
    pid=request.POST['txt1']
    fullname=request.POST['txt2']
    contactaddress=request.POST['txt3']
    p1 = person.Person(pid, fullname, contactaddress)
    mydb.insertRecord(p1)
    print("Save Record Successfully")
    return redirect('/'); # Redirect to index page