from rest_framework.routers import DefaultRouter
from django.urls import include, path
from drf_playground.users.api.viewsets import UserViewSet


router = DefaultRouter()

router.register("users", UserViewSet)

app_name = "api"

urlpatterns = router.urls
urlpatterns += [path("", include("drf_playground.users.urls"))]

