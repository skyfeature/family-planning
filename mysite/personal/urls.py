from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.getimage, name='getimage'),
    path('contact/', views.contact, name='contact'),     
]
