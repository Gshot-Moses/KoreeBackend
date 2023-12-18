from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication
from .models import Contact
from .serializers import ContactSerializer

class ContactView(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [BasicAuthentication]
    
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.order_by("firstName")
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'firstName': request.data.get('firstName'), 
            'lastName': request.data.get('lastName'), 
            'gender': request.data.get('gender'), 
            'address': request.data.get('address'), 
            'phoneNumber': request.data.get('phoneNumber'), 
            'mailAdress': request.data.get('mailAdress'), 
            'photoLink': request.data.get('photoLink'), 
        }
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ContactDetailsView(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [BasicAuthentication]

    def put(self, request, contactId, *args, **kwargs):
        contact = self.get_object(contactId)
        if not contact:
            return Response(
                {"res": "Object with contact id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'firstName': request.data.get('firstName'), 
            'lastName': request.data.get('lastName'), 
            'gender': request.data.get('gender'), 
            'address': request.data.get('address'), 
            'phoneNumber': request.data.get('phoneNumber'), 
            'mailAddress': request.data.get('mailAddress'), 
            'photoLink': request.data.get('photoLink'), 
        }
        serializer = ContactSerializer(instance = contact, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, contactId, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        contact = self.get_object(contactId)
        if not contact:
            return Response(
                {"res": "Object with contact id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        contact.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    
    def get_object(self, todo_id):
        try:
            return Contact.objects.get(id=todo_id)
        except Contact.DoesNotExist:
            return None
