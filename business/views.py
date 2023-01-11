from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .functions import *
import json


def home(request):
    return render(request, 'business/index.html', {})

@csrf_exempt
def whatsAppWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = '634dc8ab-f158-4fcc-a43a-669fc7bc8112'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('error', status=403)

    if request.method == 'POST':
        data = json.loads(request.body)
        return HttpResponse('success', status=200)
            
