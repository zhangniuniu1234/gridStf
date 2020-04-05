from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework import  viewsets
import time
# Create your views here.
from App.serializers import UserSerializer, GroupSerializer

#缓存时间60s
@cache_page(60)
def index(request):
    time.sleep(10)
    return HttpResponse("hello index")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#发邮件
def  send(request):
    subject="hello,测试"
    msg="加油，你可以的"
    send_email=["zhangniuniu@guazi.com"]
    from_email="n1997z@163.com"

    send_mail(subject,msg,from_email,send_email)
    return HttpResponse("发送成功")

