from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

router_v1 = DefaultRouter()
router_v1.register(r'tasks', TaskViewSet, basename='tasks')


urlpatterns = [
    path('', include(router_v1.urls)),
]
