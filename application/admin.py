from django.contrib import admin
from .models import restaurante, comentario, reserva

admin.site.register(restaurante)
admin.site.register(reserva)
admin.site.register(comentario)
