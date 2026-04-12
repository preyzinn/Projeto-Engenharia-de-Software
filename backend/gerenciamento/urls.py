from django.urls import path
from . import views

app_name = 'gerenciamento'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('selecao_empresa/', views.selecao_empresa, name='selecao_empresa'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projeto/<int:project_id>/', views.project_detail, name='detalhes_projeto'),
]
