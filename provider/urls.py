from django.urls import path
from .views import ProviderGenericAPIView

urlpatterns = [
    path('', ProviderGenericAPIView.as_view()),
    path('<str:pk>', ProviderGenericAPIView.as_view()),
]