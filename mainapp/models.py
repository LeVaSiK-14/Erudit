from django.db import models

class Teacher(models.Model):

    first_name = models.CharField(max_length=127, verbose_name='Имя учителя')
    last_name = models.CharField(max_length=127, verbose_name='Фамилия учителя', null=True)
    patronymic = models.CharField(max_length=127, verbose_name='Отчество учителя', null=True)
    about = models.TextField(verbose_name='О преподователе')
    image = models.ImageField(upload_to='media/mainapp/images', null=True, blank=True, verbose_name='Фото учителя')

    def __str__(self):
        return f'{self.first_name} - {self.patronymic}'

class Subject(models.Model):

    subject_name = models.CharField(max_length=127, verbose_name='Название предмета')
    duration = models.PositiveIntegerField(default=0)
    about = models.TextField()
    image = models.ImageField(upload_to='media/mainapp/images', null=True, blank=True)

    def __str__(self):
        return f'{self.subject_name}'