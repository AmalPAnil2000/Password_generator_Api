from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import generate_password

@api_view(['GET'])
def generate_password_api(request):
    length = int(request.GET.get('length', 12))
    uppercase = bool(request.GET.get('uppercase', True))
    lowercase = bool(request.GET.get('lowercase', True))
    digits = bool(request.GET.get('digits', True))
    special = bool(request.GET.get('special', True))

    # Validate input here
    if length < 4 or length > 128:
        return Response({'error': 'Password length must be between 4 and 128 characters.'})

    password = generate_password(length=length, uppercase=uppercase, lowercase=lowercase, digits=digits, special=special)
    return Response({'password': password})

