from django.urls import path
from .views import *

urlpatterns = [
    path('stud/',students_list_or_create),
    path('stud/<int:pk>',students_get_or_update)
]

