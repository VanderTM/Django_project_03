
from django.urls import path,include
from .views import SignUpView

urlpatterns=[

    path("account",include("django.contrib.auth.urls")),
    path("",SignUpView.as_view(),name="signup")

]