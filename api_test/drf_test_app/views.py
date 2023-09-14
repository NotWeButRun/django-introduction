from django.shortcuts import render

from rest_framework import routers, viewsets
from .models import UserInfo
from .serializer import UserInfoSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all() # モデルのオブジェクトを取得
    serializer_class = UserInfoSerializer # シリアライザーを取得


# DefaultRouter クラスのインスタンスを代入
router = routers.DefaultRouter()
# userInfo/ にUserInfoViewSetをルーティングする
router.register('userInfo',UserInfoViewSet)
