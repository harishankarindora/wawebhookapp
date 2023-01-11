from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('94b1ddb8-edcb-4a03-9be8-248452e1a8d9', views.whatsAppWebhook, name='whatsapp-webhook'),
]