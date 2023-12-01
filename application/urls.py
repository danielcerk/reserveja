from django.urls import path
from . import views
from .views import * 

urlpatterns = [
	
	path('', views.site),
	path('restaurantes', views.index),
	path('restaurante/create', views.create),
	path('restaurante/<int:id>', views.restaurant),
	path('api/v1/', restaurantesView.as_view()),
	path('api/v1/<int:id>', restauranteView.as_view())

] 