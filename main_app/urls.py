from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('finch/', views.finch_index , name='finch'),
#  asdasfasf
]

