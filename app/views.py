from multiprocessing import context
from .forms import StudentForm
from django.shortcuts import render, redirect
from .models import Student
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    print("Helloeee")
    print('request: ',request)
    print('method :',request.method)
    print('cookies :',request.COOKIES)
    print('path  :',request.path)
    print('user  :',request.user)
    # print('meta  :',request.META)
    return HttpResponse("Hello SveM")

def homefs(request):
    return render(request,'app/index.html')


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'app/student_list.html', context)


def student_add(request):
    form = StudentForm()  # boş form render edeceğiz
    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form': form
    }
    return render(request, 'app/student_add.html', context)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form': form,
    }
    return render(request, 'app/student_update.html', context)


def student_delete(request, id):
    # student = get_object_or_404(Student, id=id)
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("list")
    return render(request, "app/student_delete.html")


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'app/student_detail.html', context)
