from django.urls import path
from .views import DepartamentosList, DepartamentoCreate, DepartamentoEdit, DepartamentoDelete

urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentoCreate.as_view(), name='departamento_create'),
    path('edit/<int:pk>', DepartamentoEdit.as_view(), name='departamento_edit'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='departamento_delete'),
]
