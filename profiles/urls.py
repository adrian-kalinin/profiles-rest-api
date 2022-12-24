from django.urls import include, path
from rest_framework.routers import DefaultRouter

from profiles import views

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")

urlpatterns = [
    path("hello-apiview/", views.HelloApiView.as_view()),
    path("", include(router.urls)),
]
