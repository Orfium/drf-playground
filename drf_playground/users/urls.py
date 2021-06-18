from django.urls import path
from drf_playground.users.api.views import SignInView

urlpatterns = [
    path(r"sign-in/", SignInView.as_view()),
]
