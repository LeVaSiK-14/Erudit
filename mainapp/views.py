from django.shortcuts import render
from mainapp.models import Teacher, Subject

def index(request):
    template_name = 'mainapp/index.html'
    return render(request, template_name)


def teachers(request):
    template_name = 'mainapp/teachers.html'
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
    }
    return render(request, template_name, context=context)


def teacher_detail(request, teacher_id):
    template_name = 'mainapp/teacher_detail.html'
    teacher = Teacher.objects.get(id=teacher_id)
    context = {
        'teacher': teacher,
    }
    return render(request, template_name, context=context)


def subjects(request):
    template_name = 'mainapp/subjects.html'
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request, template_name, context=context)

def subject_detail(request, subject_id):
    template_name = 'mainapp/subject_detail.html'
    subject = Subject.objects.get(id=subject_id)
    context = {
        'subject': subject,
    }
    return render(request, template_name, context=context)