from django.urls import path
from .views import HoraExtraList

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('novo', FuncionarioCreate.as_view(), name='funcionario_create'),
    # path('editar/<int:pk>', FuncionarioEdit.as_view(), name='funcionario_edit'),
    # path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='funcionario_delete'),
]
