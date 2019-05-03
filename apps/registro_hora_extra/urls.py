from django.urls import path
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraCreate

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', HoraExtraCreate.as_view(), name='hora_extra_create'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='hora_extra_edit'),
    path('deletar/<int:pk>', HoraExtraDelete.as_view(), name='hora_extra_delete'),
]
