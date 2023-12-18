from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "firstName", 
            "lastName", 
            "address",
            "gender", 
            "phoneNumber", 
            "mailAdress",
            "photoLink"
            ]