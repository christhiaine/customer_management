from django.shortcuts import render
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCreateView(generics.CreateAPIView):
    model = Customer
    fields = ['name', 'email', 'phone', 'date_of_birth', 'nationality', 
                  'business_name', 'business_categories', 'registration_date', 'age_of_business_in_days', 'location']
    serializer_class = CustomerSerializer

class CustomerUpdateView(generics.UpdateAPIView):
    model = Customer
    fields = ['name', 'email', 'phone', 'date_of_birth', 'nationality', 
                  'business_name', 'business_categories', 'registration_date', 'age_of_business_in_days', 'location']
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class CustomerDeleteView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    model = Customer
    success_url = '/customers'


