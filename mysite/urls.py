from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),  
    path('deviceID/', views.get_device_id, name="get_device_id"),
    path('msgSIG/', views.get_msg_sig, name="get_msg_sig"),
    path('get_weather_from_ip/', views.get_weather_from_ip, name="get_weather_from_ip"),
]