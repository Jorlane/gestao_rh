from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelete, HoraExtraCreate,
    HoraExtraEditBase,
    HoraExtraUtilizar,
    HoraExtraDesmarcaUtilizar,
    RelatorioHoraExtra
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', HoraExtraCreate.as_view(), name='hora_extra_create'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='hora_extra_edit'),
    path('editar_base/<int:pk>', HoraExtraEditBase.as_view(), name='hora_extra_edit_base'),
    path('utilizar_hora_extra/<int:pk>', HoraExtraUtilizar.as_view(), name='hora_extra_utilizar'),
    path('desmarca_utilizar_hora_extra/<int:pk>', HoraExtraDesmarcaUtilizar.as_view(), name='hora_extra_desmarca_utilizar'),
    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name='hora_extra_delete'),
    path('relatorio_hora_extra', RelatorioHoraExtra.as_view(), name='relatorio_hora_extra'),
]
