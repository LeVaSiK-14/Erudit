from django.urls import path
from mainapp.views import (
                            index, 
                            teachers, 
                            teacher_detail, 
                            subjects, 
                            subject_detail)

urlpatterns = [
    path('', index, name='index'),
    path('teachers/', teachers, name='teachers'),
    path('teacher/<int:teacher_id>/', teacher_detail, name='teacher_detail'),
    path('subjects/', subjects, name='subjects'),
    path('subject/<int:subject_id>/', subject_detail, name='subject_detail'),
]