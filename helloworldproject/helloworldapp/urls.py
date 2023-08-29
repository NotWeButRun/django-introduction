from django.urls import path
from .views import helloworldfunction

urlpatterns = [
    path("hwapp/", helloworldfunction),
]