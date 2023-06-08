from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finch/', views.finch_index , name='finch'),
    # new route below 
 path('finch/<int:finch_id>/', views.finch_detail, name='finch_detail'),
]

