from django.shortcuts import render, redirect, get_object_or_404
from .forms import NovoUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.core.files.storage import default_storage
from django.conf import settings



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
