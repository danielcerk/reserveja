from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

from application.models import *

# {"nome":"Pode ser qualquer um","descricao":"nenhuma","user":2}

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

