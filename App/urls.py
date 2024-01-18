# your_app_name/urls.py
from django.urls import path
from .views import example_page

urlpatterns = [
    path('login/', login, name='login'),
]
