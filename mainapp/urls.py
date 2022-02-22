from django.urls import path
from mainapp.views import (
                            index,
                            subject_detail,
                            send
)

urlpatterns = [
    path('', index, name='index'),
    path('subject/<int:subject_id>/', subject_detail, name='subject_detail'),
    path('form/', send, name='form')
]