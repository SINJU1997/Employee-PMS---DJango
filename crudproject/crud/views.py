from django.shortcuts import render,redirect
from django .http import HttpResponse
from . models import Employee

# Create your views here.

def index(request):
    return render(request,'index.html')

def newEmployee(request):
    return render(request,'register.html')

def addEmployee(request):
    if request.method=="POST":
        employee_name=request.POST.get('empname')
        employee_place=request.POST.get('empplace')
        employee_phone=request.POST.get('empphone')
        employee_designation=request.POST.get('empdesignation')
        query=Employee(Name=employee_name,Place=employee_place,Phoneno=employee_phone,Designation=employee_designation)
        query.save()
        return redirect('/')
def viewEmployees(request):
    employee_data={
        'employees':Employee.objects.all()
    }
    return render(request,'employees.html',employee_data)

def deleteEmployee(request,id):
    delete_data=Employee.objects.get(id=id)
    delete_data.delete()
    return redirect('/')

def editEmployee(request,id):
    data={
        'employee':Employee.objects.get(id=id)
    }
    return render(request,'edit.html',data)

def updateEmployee(request,id):
    if request.method=="POST":
        ename=request.POST.get('empname')
        eplace=request.POST.get('empplace')
        ephoneno=request.POST.get('empphone')
        eplace=request.POST.get('empplace')
        edesignation=request.POST.get('empdesignation')

        edit_data=Employee.objects.get(id=id)

        edit_data.Name=ename
        edit_data.Place=eplace
        edit_data.Phoneno=ephoneno
        edit_data.Designation=edesignation
        edit_data.save()
        return redirect('/')

