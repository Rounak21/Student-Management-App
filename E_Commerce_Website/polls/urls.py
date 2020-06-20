from django.urls import path
from .views import home, details

urlpatterns = [
    path('',home, name="home"),
    path('<int:id>/', details, name="post-detail"),
    path('details/', details, name="post-entry"),
]