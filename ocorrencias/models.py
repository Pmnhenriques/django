from django.db import models

class Ocorrencias(models.model):
	descricao = models.TextField()
	localizacao = models.CharField(max_length = 200)
	autor = models.ForeignKey(Autor, null=True, blank=True)
	dataCriacao = models.DateTimeField()
	dataActualizacao = models.DateTimeField()
	estado = models.ForeignKey(Estado, null=True, blank=True)
	estado = models.ForeignKey(Estado, null=True, blank=True)


class Estado(models.Model):
    estado = models.IntegerField(default='0') # estado 0: por validar | 1: validado | 2:resolvido



