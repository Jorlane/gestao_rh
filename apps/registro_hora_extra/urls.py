from django.urls import path
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraCreate, HoraExtraEditBase

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', HoraExtraCreate.as_view(), name='hora_extra_create'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='hora_extra_edit'),
    path('editar_base/<int:pk>', HoraExtraEditBase.as_view(), name='hora_extra_edit_base'),
    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name='hora_extra_delete'),
]
