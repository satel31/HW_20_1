from django.shortcuts import render
from apps.catalog.models import Product, Contacts

# Create your views here.
def homepage(request):
    data = Product.objects.order_by('-creation_date')[:5]
    for d in data:
        print(d)
    return render(request, 'homepage.html')

def contacts(request):
    context = {'contact': []}
    for contact in Contacts.objects.all():
        context['contact'].append({'first_name': contact.first_name, 'last_name': contact.last_name, 'phone': contact.phone, 'email': contact.email})
    return render(request, 'contacts.html', context=context)
