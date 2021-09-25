from django.urls import path
from basicapp import views
app_name = 'basic_app'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('customer/',views.CustomersListView.as_view(),name='customers'),
    path('customer/<pk>/',views.CustomerDetailView.as_view(),name='detail'),
    path('transfer/',views.TransfersListView.as_view(),name='transfers'),
    path('create/',views.CustomerCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.CustomerUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.CustomerDeleteView.as_view(),name='delete'),
    path('formpage/',views.transferForm,name='formpage'),

]
