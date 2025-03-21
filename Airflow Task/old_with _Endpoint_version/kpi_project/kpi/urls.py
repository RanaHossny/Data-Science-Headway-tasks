from django.urls import path
from . import views

urlpatterns = [
    path('kpis/', views.kpi_list_create, name='kpi_list_create'),
    path('link_asset/', views.link_asset_to_kpi, name='link_asset_to_kpi'),
    path('simulators/', views.Simulator_veiw, name='simulator-list-create'),
    path('asset-attributes/', views.Attribute_veiw, name='asset-attribute-list-create'),

]
