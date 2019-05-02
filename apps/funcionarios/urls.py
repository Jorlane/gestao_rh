from django.urls import path
from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete, FuncionarioCreate

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo', FuncionarioCreate.as_view(), name='funcionario_create'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='funcionario_edit'),
    path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='funcionario_delete'),
]
