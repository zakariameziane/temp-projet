from django.urls import path
from . import views
from . import api
from django.contrib.auth import views as auth_views
from .views import register_request, login_request, logout_request

urlpatterns = [
    # API endpoints
    path("api/", api.Dlist, name='json'),
    path("api/post/", api.Dlist, name='json-post'),

    # Temperature data views
    path('download_csv/', views.download_csv, name='download_csv'),
    path('', views.home, name='index'),
    path('table/', views.table, name='table'),

    # Chart views
    path('chart-temp/', views.graphiqueTemp, name='myChartTemp'),
    path('chart-hum/', views.graphiqueHum, name='myChartHum'),
    path('chart-data/', views.chart_data, name='chart-data'),

    # Time-based chart data
    path('chart-data-jour/', views.chart_data_jour, name='chart-data-jour'),
    path('chart-data-semaine/', views.chart_data_semaine, name='chart-data-semaine'),
    path('chart-data-mois/', views.chart_data_mois, name='chart-data-mois'),

    # Authentication views (using your custom views)
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),


]