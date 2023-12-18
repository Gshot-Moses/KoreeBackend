#from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken import views
from .views import ContactView, ContactDetailsView

urlpatterns = [
    path('', ContactView.as_view()),
    path('<int:contactId>/', ContactDetailsView.as_view()),
]