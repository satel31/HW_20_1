from django.urls import path
from apps.catalog.views import homepage

app_name = 'catalog'

urlpatterns = [
    path('', homepage),
]