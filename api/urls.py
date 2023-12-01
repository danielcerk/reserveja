from .views import * 
from django.urls import path

urlpatterns = [

	path('', restaurantesView.as_view()),
	path('<int:id>', restauranteView.as_view())

] 