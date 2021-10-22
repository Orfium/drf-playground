from django.urls import include, path
from drf_playground.files.api.viewsets import FileViewSet
from drf_playground.users.api.viewsets import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("users", UserViewSet)
router.register("files", FileViewSet)

app_name = "api"

urlpatterns = router.urls
urlpatterns += [path("", include("drf_playground.users.urls"))]
urlpatterns += [path("", include("drf_playground.files.urls"))]
