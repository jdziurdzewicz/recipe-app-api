"""
URL mappings for the recipes APIs
"""
from django.urls import path, include
from recipe import views
from rest_framework.routers import DefaultRouter

app_name = 'recipe'

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]