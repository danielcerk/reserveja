from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NovoUserForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].help_text = None

	email = forms.EmailField(required=True)


	class Meta:

		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def save(self, commit=True):

		user = super(NovoUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:

			user.save()

		return user