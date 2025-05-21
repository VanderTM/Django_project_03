
from django.urls import path,include
from .views import SignUpView, HomeView

urlpatterns=[

    path("account",include("django.contrib.auth.urls")),
    path("registro/signup",SignUpView.as_view(),name="signup"),
    path ("",HomeView.as_view(),name='home')


]