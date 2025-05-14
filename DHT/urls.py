from django.urls import path
from . import views
from . import api
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("api/", api.Dlist, name='json'),
    path("api/post/", api.Dlist, name='json-post'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('', views.home, name='index'),
    path('table/', views.table, name='table'),

    path('chart-temp/', views.graphiqueTemp, name='myChartTemp'),
    path('chart-hum/', views.graphiqueHum, name='myChartHum'),
    path('chart-data/', views.chart_data, name='chart-data'),

    path('chart-data-jour/', views.chart_data_jour, name='chart-data-jour'),
    path('chart-data-semaine/', views.chart_data_semaine, name='chart-data-semaine'),
    path('chart-data-mois/', views.chart_data_mois, name='chart-data-mois'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]