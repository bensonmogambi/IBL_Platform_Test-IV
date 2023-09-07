import logging
import requests
import json
import urllib.parse

from .models import Greeting
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



# Create your views here.

#from django.shortcuts import render

#def home(request):
    #return render(request, 'myapp/home.html')


logger = logging.getLogger(__name__)


def make_api_call(endpoint, data, request):
    access_token = request.auth.token


    host = request.META['HTTP_HOST']
    api_url = f'{request.scheme}://{host}/{endpoint}/'
    
    headers = {'Authorization': f'Bearer {access_token}'}
    
    response = requests.post(api_url, data=data, headers=headers)

    if response.status_code == 200:
        data = response.json()    
    return response


@api_view(['POST'])
def greeting(request):
    greeting = request.data.get('greeting', None)

    if greeting is None:
        return Response({"message":"No greeting passed", "info": "Parameter 'greeting' must have a value."}, status=status.HTTP_400_BAD_REQUEST)
    print(greeting)

    logger.info(f"User greeting: {greeting}")

    s = Greeting.objects.create(user=request.user,body=greeting)

    if greeting == 'hello':
        response = make_api_call('api/greeting', {'greeting': 'goodbye'}, request)

    return Response({'message': 'Hello, user! Greeting saved successfully!'}, status=status.HTTP_200_OK)