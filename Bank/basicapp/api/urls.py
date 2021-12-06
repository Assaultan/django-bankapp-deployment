from django.urls import path
from basicapp.api.views import customer_list,customer_detail

urlpatterns = [
    path('list/',customer_list, name='customer-list'),
    path('<int:pk>/',customer_detail, name='customer-detail'),
]