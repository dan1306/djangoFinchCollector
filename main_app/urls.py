from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finch/', views.finch_index , name='finch'),
    # new route below 
    path('finch/<int:finch_id>/', views.finch_detail, name='finch_detail'),
    path('finch/create/', views.FinchCreate.as_view(), name='finch_create'),
    # Add the new routes below
    path('finch/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('finch/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete')
]

