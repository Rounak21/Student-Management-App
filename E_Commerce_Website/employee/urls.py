from django.urls import path
from .views import *

urlpatterns = [
    path('', lists, name="employee-list"),
    path('<int:id>/details/', detail, name="employee-detail"),
    path('add/',add, name="employee-add"),
    path('<int:id>/edit/', edit, name="employee-edit"),
    # path('details/id')
]
