from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'advs', views.AdvantageItemViewSet)
router.register(r'links', views.HeaderLinkViewSet)


urlpatterns = [
    path('', include(router.urls))
]