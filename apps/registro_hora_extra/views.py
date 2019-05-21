import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views.generic.base import View

from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm

import csv

class HoraExtraList(ListView):
    model = RegistroHoraExtra()
    fields = ['motivo', 'funcionario', 'horas']

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)

class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    # success_url = reverse_lazy('list_hora_extra')

    def get_success_url(self):
        return reverse_lazy('hora_extra_edit_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraUtilizar(View):
    def post(self, *args, **kwargs):

        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])

        registro_hora_extra.utilizada = True

        registro_hora_extra.save()

        funcionario = registro_hora_extra.funcionario
        total = funcionario.total_horas

        response = json.dumps({'mensagem': 'Hora extra marcada como utilizada', "total_horas": float(total)})
        return HttpResponse(response, content_type='application/json')

class HoraExtraDesmarcaUtilizar(View):
    def post(self, *args, **kwargs):

        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])

        registro_hora_extra.utilizada = False

        registro_hora_extra.save()

        funcionario = registro_hora_extra.funcionario
        total = funcionario.total_horas

        response = json.dumps({'mensagem': 'Hora extra desmarcada como utilizada', "total_horas": float(total)})
        return HttpResponse(response, content_type='application/json')

class RelatorioHoraExtra(View):
    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        registros = RegistroHoraExtra.objects.filter(utilizada=False,funcionario__empresa=request.user.funcionario.empresa)

        writer = csv.writer(response)
        writer.writerow(['Id', 'Motivo', 'Funcionario', 'Saldo', 'Horas'])

        for reg in registros:
            writer.writerow([reg.id, reg.motivo, reg.funcionario, reg.funcionario.total_horas, reg.horas])

        return response