from django.urls import path
from basicapp import views

urlpatterns=[
    path('home/',views.homepage,name='home'),
    path('customer/',views.customers,name='customer'),
    path('formpage/',views.transferForm,name='formpage'),
    path('transfers/',views.transfers,name='transfers'),
]
