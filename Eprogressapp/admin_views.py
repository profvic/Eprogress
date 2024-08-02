from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from Eprogressapp.models import CustomUser, Departments


def admin_home(request):
    return render(request, 'course_adviser_template/home_content.html')

def add_lecturer(request):
    return render(request, 'course_adviser_template/add_lecturer.html')

def add_lecturer_save(request):
    if request.method!='POST':
        return HttpResponse('Method not Allowed')
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        username=request.POST.get("username")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.lecturers.address=address
            user.save()
            messages.success(request, "Successfully Added Lecturer")
            return HttpResponseRedirect('/add_lecturer')

        except:
            messages.error(request, "Failed to Add Lecturer")
            return HttpResponseRedirect('/add_lecturer')

def add_student(request):
    return render(request, 'course_adviser_template/add_student.html')

def add_student_save(request):
    if request.method!='POST':
        return HttpResponse('Method not Allowed')
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        username=request.POST.get("username")
        address=request.POST.get("address")
        session_start = request.POST.get('session_start')
        session_end=request.POST.get('session_end')
        sex=request.POST.get('sex')

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name, session_start=session_start, session_end=session_end, sex=sex, user_type=3)
            user.students.address=address
            user.save()
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect('/add_student')

        except:
            messages.error(request, "Failed to Add Student")
            return HttpResponseRedirect('/add_student')
        
def add_department(request):
    return render(request, 'course_adviser_template/add_department.html')

def add_department_save(request):
    if request.method!='POST':
        return HttpResponse('Method not Allowed')
    else:
        department = request.POST.get('department')
        try:
            department_model= Departments(department_name=department)
            department_model.save()
            messages.success(request, 'Successfully Added Department')
            return HttpResponseRedirect('/add_department')
        except:
            messages.error(request, 'Failed to Add Department')
            return HttpResponseRedirect('/add_department')
