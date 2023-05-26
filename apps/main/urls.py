from django.urls import path
from apps.main.views import index

app_name = 'catalog'

urlpatterns = [
    path('', index),
]