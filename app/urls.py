from django.urls import path
from app import views

urlpatterns = [
    path('mint', views.NFTView.as_view({'post': 'create','get': 'list'}), name='create-mint'),
    path('mint/<str:pk>', views.NFTView.as_view({'get': 'retrieve'}), name='retrieve-mint'),
    
]