"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# project setup (only added include to this import)
from django.urls import include, path
# project setup
from rest_framework.routers import DefaultRouter
from api.views import PetBehaviorViewSet, PostViewSet

# project setup
router = DefaultRouter(trailing_slash=False)
# initial view setup
router.register(r"petbehaviors", PetBehaviorViewSet, "petbehavior")
router.register(r"posts", PostViewSet, "post")

urlpatterns = [
    # project setup (start fresh)
    path("", include(router.urls)),
]
