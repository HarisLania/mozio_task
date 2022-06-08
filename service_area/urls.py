from django.urls import path
from .views import ServiceAreaGenericAPIView, PolygonsAPIView

urlpatterns = [
    path('', ServiceAreaGenericAPIView.as_view()),
    path('<str:pk>', ServiceAreaGenericAPIView.as_view()),
    path('<lat>/<long>', PolygonsAPIView.as_view({
                                        'get': 'list'
                                        }))
]