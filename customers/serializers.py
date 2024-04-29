from  rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    age_of_business_in_days = serializers.IntegerField(read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'date_of_birth', 'nationality', 
                  'business_name', 'business_categories', 'registration_date', 'age_of_business_in_days', 'location']