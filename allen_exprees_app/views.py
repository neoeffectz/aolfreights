from django.shortcuts import render
from django.contrib.auth.models import  auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Shipping
from .forms import ShippingForm
from django.db.models import Q
from .forms import UserForm

# Create your views here.



def home(request):

    
    return render(request, 'home.html')

def about_us(request):

    
    return render(request, 'about-us.html')

def signin(request):

    
    return render(request, 'login.html')

def contact_us(request):

    
    return render(request, 'contact.html')


@login_required(login_url='signin')
def create_shipping(request):

    form_name = ShippingForm()
    if request.method == 'POST':
        form_name = ShippingForm(request.POST)
    if form_name.is_valid():
            shipping_form = form_name.save(commit=False)
            shipping_form.user = request.user
            shipping_form.save()
            form_name = ShippingForm()
            return redirect('dashboard')
            

    
    return render(request, 'create-shipment.html', {'form_name': form_name} )




def shipping_details(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        if query:
            results = Shipping.objects.filter(Q(tracking_number__icontains=query))
        else:
            results = Shipping.objects.none()

        context = {
            'query': query,
            'results': results,
        }

        return render(request, 'shipping-details.html', context)
    else:
        return render(request, 'shipping-details.html')
    

def logout(request):
    auth.logout(request)
    return redirect('signin')
