from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers

from App import views

router=routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^sendmail/',views.send)
]