from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from .models import Course
from django.shortcuts import render



def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_details.html', {'course': course})

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})
