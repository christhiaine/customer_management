from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
class CustomerListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'

class CustomerUpdateView(generics.UpdateAPIView):
    serializer_class = CustomerSerializer   
    queryset = Customer.objects.all()

class CustomerDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    model = Customer
    success_url = '/customers'


