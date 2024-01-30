from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('submit/',CreateForm.as_view()),
    path('get/',GetForm.as_view()),
    path('delete/<int:pk>',DeleteForm.as_view()),
    path('update/<int:pk>',UpdateForm.as_view()),
]