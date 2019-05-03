from django.forms import ModelForm

from apps.funcionarios.models import Funcionario
from .models import RegistroHoraExtra

class RegistroHoraExtraForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        empresa_logada = user.funcionario.empresa
        self.fields['funcionario'].queryset = Funcionario.objects.filter(empresa=empresa_logada)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']