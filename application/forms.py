from .models import restaurante
from django import forms

class restauranteForm(forms.ModelForm):

	class Meta:

		model = restaurante
		fields = ('nome', 'descricao', 'foto')