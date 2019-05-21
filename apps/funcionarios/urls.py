from django.urls import path
from .views import (
    FuncionariosList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioCreate,
    FuncionarioRelatorio,
    Pdf
)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo', FuncionarioCreate.as_view(), name='funcionario_create'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='funcionario_edit'),
    path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='funcionario_delete'),
    path('relatorio_funcionarios', FuncionarioRelatorio, name='relatorio_funcionarios'),
    path('relatorio_funcionarios_html', Pdf.as_view(), name='relatorio_funcionarios_html'),
]
