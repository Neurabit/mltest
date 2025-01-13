from django.urls import path
from .views import userview

urlpatterns = [
    path("", userview, name='users')
]