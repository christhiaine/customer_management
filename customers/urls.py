from django.urls import path
from .views import CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer-create'),
    path('customers/update/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer-delete'),
]
