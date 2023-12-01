from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import restauranteForm
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

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


# API


class restaurantesView(APIView):

	def get(self, request):

		restaurantes = restaurante.objects.all()
		serializer = restauranteSerializer(restaurantes, many=True)

		return Response(serializer.data)

	
	def post(self, request):

		serializer = restauranteSerializer(data=request.data)

		if serializer.is_valid():

			serializer.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class restauranteView(APIView):

	def get(self, request, id):

		restaurantes = restaurante.objects.filter(pk=id).first()

		serializer = restauranteSerializer(restaurantes, many=False)

		return Response(serializer.data)


	def delete(self, request, id):

		restaurante_item = restaurante.objects.get(pk=id)

		if restaurante_item:

			restaurante_item.delete()

			return Response({'204': 'Nenhum conteudo'}, status=status.HTTP_204_NO_CONTENT)

		else:

			return Response({'erro': 'Página não encontrada'}, status=status.HTTP_404_NOT_FOUND)
