from django.shortcuts import render, redirect, get_object_or_404
from .forms import NovoUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.core.files.storage import default_storage
from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .serializers import *

class RegisterAPIView(APIView):

	permission_classes = [AllowAny]

	def post(self, request):

		serializer = RegisterSerializer(data=request.data)

		if serializer.is_valid():

			username = serializer.validated_data['username']
			password = serializer.validated_data['password']

			if User.objects.filter(username=username).exists():

				return Response({'erro':'nome de usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)

			else:

				return Response({'sucesso':'Usuário registrado com sucesso'},
				 status=status.HTTP_201_CREATED)

		else:

			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):

	permission_classes = [AllowAny]

	def post(self, request):

		serializer = LoginSerializer(data=request.data)

		if serializer.is_valid():

			username = serializer.validated_data['username']
			password = serializer.validated_data['password']

			user = authenticate(username=username, password=password)

			if user is not None:

				login(request, user)
				user_serializer = UserSerializer(user)

				return Response({'sucesso': 'Login foi um sucesso'}, status=status.HTTP_200_OK)

			else:

				return Response({'error': 'Nome de usuário e/ou senha incorretos'}, status=status.HTTP_401_UNAUTHORIZED)

		else:

			return Response(serializer.errors,
				status=status.HTTP_400_BAD_REQUEST)


# Login do usuario

def login_request(request):

	search = request.GET.get('search') # Barra de pesquisa

	if request.method == 'POST':

		form = AuthenticationForm(request, data=request.POST)

		if form.is_valid():

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')

			users = authenticate(username=username, password=password)

			if users is not None:

				login(request, users)

				return redirect(request.GET.get('next', '/'))

			else:

				messages.error(request, 'Username ou senha inválidos!')

		else:

			messages.error(request, 'Username ou senha inválidos!')


	else:

		# PESQUISAR ITEM


		if search:

			return redirect(f'/?search={search}')



	form = AuthenticationForm()


	return render(request=request,
	 template_name='registration/login.html',
	 context={'login_form': form})


# Registrar usuario

def register(request):

	search = request.GET.get('search') # Barra de pesquisa

	if request.method == 'POST':

		form = NovoUserForm(request.POST)

		if form.is_valid():

			users = form.save()

			login(request, users)

			messages.success(request, 'Registro concluído!')

			return redirect('/')

		messages.error(request, 'Registro não foi concluído . Username ou email existentes!')


	else:

		# PESQUISAR ITEM

		if search:

			return redirect(f'/?search={search}')


	form = NovoUserForm()

	return render(request=request, 
		template_name='registration/register.html',
		context={'register_form': form})


# Conta

@login_required(login_url='/login')
def account(request):

	search = request.GET.get('search') # Barra de pesquisa

	user = request.user


	if search:

		return redirect(f'/?search={search}')

	return render(request, 'registration/account.html', {'user': user})





