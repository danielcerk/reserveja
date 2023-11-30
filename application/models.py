from django.contrib.auth import get_user_model
from django.db import models

class restaurante(models.Model):

	nome = models.CharField(max_length=120)
	descricao = models.TextField()
	foto = models.ImageField(null=True, blank=True, upload_to='images/',
		default='images/not-found.jpg')
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return self.nome


class reserva(models.Model):

	restaurante_id = models.ForeignKey(restaurante, on_delete=models.CASCADE)
	data = models.DateField()
	hora = models.TimeField()
	numero_pessoas = models.IntegerField(default=1)
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


	def __str__(self):

		return self.restaurante_id

class comentario(models.Model):

	restaurante_id = models.ForeignKey(restaurante, on_delete=models.CASCADE)
	texto = models.TextField()
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return self.restaurante_id


