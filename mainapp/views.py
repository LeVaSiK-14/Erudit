from django.shortcuts import render
from mainapp.models import Teacher, Subject

def index(request):
    template_name = 'mainapp/index.html'
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    context = {
        "teachers": teachers,
        "subjects": subjects,
    }
    return render(request, template_name, context=context)


def subject_detail(request, subject_id):
    template_name = 'mainapp/subject_detail.html'
    subject = Subject.objects.get(id=subject_id)
    context = {
        'subject': subject,
    }
    return render(request, template_name, context=context)