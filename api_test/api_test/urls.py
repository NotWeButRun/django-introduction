from django.contrib import admin
from django.urls import path,include


from drf_test_app import views


urlpatterns = [
    path('admin/',admin.site.urls),
    # defaultRouter をinclude する
    path('api/',include(views.router.urls)),
]