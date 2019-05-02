from django.views.generic import ListView
from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra()
    fields = ['motivo', 'funcionario', 'horas']

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
