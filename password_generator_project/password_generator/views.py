# views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import generate_password

@api_view(['GET'])
def generate_password_api(request):
    choices = request.GET.getlist('choices', ['uppercase', 'lowercase', 'digits', 'special'])
    length = int(request.GET.get('length', 12))

    try:
        password = generate_password(length=length, choices=choices)
        return Response({'password': password})
    except ValueError as e:
        return Response({'error': str(e)}, status=400)