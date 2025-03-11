from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrchestraList.as_view(), name='start'),
]
