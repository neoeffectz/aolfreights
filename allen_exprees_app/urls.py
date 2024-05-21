from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name = 'home' ),
    path('about-us/', views.about_us, name = 'aboutus' ),
    path('contact-us/', views.contact_us, name = 'contactus' ),    
    path('signin/', views.signin, name = 'signin' ),   
    path('create-shipping/', views.create_shipping, name = 'createshipping' ),
    path('shipping-details/', views.shipping_details, name = 'shippingdetails' ),
    path('logout', views.logout, name = 'logout'),     
]