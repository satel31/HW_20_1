from django.urls import path
from apps.catalog.views import index

app_name = 'catalog'

urlpatterns = [
    path('', index),
]