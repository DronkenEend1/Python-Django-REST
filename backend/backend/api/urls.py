from django.urls import path
from . import views


urlpatterns = [
    # localhost:8000/api/
    path('', views.api_home)
]