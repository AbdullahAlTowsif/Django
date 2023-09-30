from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='homepage'),
    path('show/',views.showData, name='showData')
]
