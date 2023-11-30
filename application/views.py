from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import restauranteForm
from .models import *

def site(request):

	return render(request, 'application/ladingpage.html')

def index(request):

	restaurantes = restaurante.objects.all().order_by('created_at')

	return render(request, 'application/index.html',
	 {'restaurantes': restaurantes})


@login_required(login_url='login/')
def create(request):

	if request.method == 'POST':

		form = restauranteForm(request.POST, request.FILES)

		if form.is_valid():

			restaurante_add = form.save(commit=False)

			restaurante_add.user = request.user

			restaurante_add.save()

			print('Restaurante adicionado')

			return redirect('/restaurantes')

	else:

		form = restauranteForm()

	return render(request, 'application/create.html', {'form': form})


def restaurant(request, id):

	restaurante_info = get_object_or_404(restaurante, pk=id)
	comentarios = comentario.objects.filter(restaurante_id=restaurante_info).all()
	reservas = reserva.objects.filter(restaurante_id=restaurante_info).all()

	if request.method == 'POST':

		submit = request.POST.get('submit')

		if submit == 'postar_comentario':

			texto = request.POST.get('comentario')

			postar_comentario = comentario.objects.create(

					restaurante_id=restaurante_info, texto=texto,
					user=request.user

				)

			postar_comentario.save()

			print('Comentário postado')


		elif submit == 'reservar':

			data = request.POST.get('date')
			hora = request.POST.get('time')
			numero_de_pessoas = request.POST.get('number')

			criar_reserva = reserva.objects.create(

					restaurante_id=restaurante_info, data=data,
					hora=hora, numero_pessoas=numero_de_pessoas,
					user=request.user
				)

			criar_reserva.save()

			print('Reserva realizada') 

	return render(request, 'application/restaurant.html',
		{'restaurante': restaurante_info,
		'comentario': comentarios,
		'reserva': reservas})