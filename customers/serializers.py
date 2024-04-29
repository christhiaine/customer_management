from datetime import date
from  rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):


    age_of_business_in_days = serializers.SerializerMethodField()
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'date_of_birth', 'nationality', 
                  'business_name', 'business_categories', 'registration_date', 'age_of_business_in_days', 'location']
        
    def get_age_of_business_in_days(self, obj):
        registration_date = obj.registration_date
        today = date.today()
        age_of_business_in_days = (today - registration_date).days
        return age_of_business_in_days
    
