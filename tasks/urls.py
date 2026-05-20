from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from . import views  # To access previous views if needed

# Building an automatic router for a new API
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # Old addresses (I commented them out so there is no confusion)
    # path('', views.home_view, name='home'),
    # path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    # path('complete/<int:pk>/', views.complete_task, name='complete_task'),

    # New address to connect to Vue.js
    path('api/', include(router.urls)),
]