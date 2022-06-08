from django.urls import path
from .views import ProviderAPIView

urlpatterns = [
    path('', ProviderAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<str:pk>', ProviderAPIView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]