from django.shortcuts import render
from apps.catalog.models import Product

# Create your views here.
def homepage(request):
    data = Product.objects.order_by('-creation_date')[:5]
    for d in data:
        print(d)
    return render(request, 'homepage.html')