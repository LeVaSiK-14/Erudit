
from django.shortcuts import render, redirect
from mainapp.models import Teacher, Subject, Mail
from mainapp.tasks import send_mail_to_gmail

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


def send(request):
    name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone_number = request.POST.get('phone_number')
    text = request.POST.get('text')
    print(email)
    send_mail_to_gmail.delay(
        name,
        last_name,
        email,
        phone_number,
        text)
    print('-'*20, 1)
    Mail.objects.create(
        name=name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        text=text)
    return redirect('index')