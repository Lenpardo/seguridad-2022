from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@csrf_exempt
@api_view(['POST'])


def loginValidation(request):
	data = JSONParser().parse(request)
	
	# user = User.objects.create_user('prueba', 'len.pardo@duocuc.cl', 'prueba')
	# user.first_name = 'prueba'
	# user.last_name = 'dos'
	# user.save()

	username = data['username']
	password = data['password']

	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		return Response("Usuario invÃ¡lido")

	#validamos la pass
	pass_valido = check_password(password, user.password)

	if not pass_valido:
		return Response("Password incorrecta")

	#permite crear o recuperar el token
	token, created = Token.objects.get_or_create(user=user)
	#print(token.key)
	return Response(token.key)