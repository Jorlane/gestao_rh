from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    @property
    def total_horas(self):
        total =  self.registrohoraextra_set.filter(utilizada=False).aggregate(Sum('horas'))
        return total['horas__sum'] or 0


    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.nome
