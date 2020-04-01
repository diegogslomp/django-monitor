from django.urls import path
from . import views

app_name = 'monitor'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('host_list', views.HostListView.as_view(), name='host_list'),
    path('ports', views.PortView.as_view(), name='ports'),
    path('port_list', views.PortListView.as_view(), name='port_list'),
    path('<int:pk>/', views.HostDetailView.as_view(), name='detail'),
]
