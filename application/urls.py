from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.site),
	path('/restaurantes', views.index),
	path('restaurante/create', views.create),
	path('restaurante/<int:id>', views.restaurant),
	path('restaurante/d/<int:id>', views.delete_restaurant)

]