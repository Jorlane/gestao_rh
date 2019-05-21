from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
import io
from django.http import FileResponse, HttpResponse
from django.views.generic.base import View
from reportlab.pdfgen import canvas

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

from apps.funcionarios.models import Funcionario

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamento']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamento']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        nomesplited = funcionario.nome.split(' ')
        username = nomesplited[0]
        if len(nomesplited) > 1:
            username = username + nomesplited[1]

        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)

def FuncionarioRelatorio(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)
    p.drawString(10, 810, 'Relatório de Funcionários')
    p.drawString(0, 800, '_' * 150)

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    str_ = 'Nome: %s | Horas Extras: %.2f'

    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (funcionario.nome, funcionario.total_horas))
        y = y - 40

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(html.encode("UTF-8"), response)

        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):
    def get(self, request):

        funcionarios = Funcionario.objects.all()
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'funcionarios': funcionarios,
            'request': request,
        }

        return Render.render('funcionarios/relatorio.html', params, 'myfile')
