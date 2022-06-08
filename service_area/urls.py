from django.urls import path
from .views import ServiceAreaAPIView, PolygonsAPIView

urlpatterns = [
    path('', ServiceAreaAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<str:pk>', ServiceAreaAPIView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('<lat>/<long>', PolygonsAPIView.as_view({
                                        'get': 'list'
                                        }))
]