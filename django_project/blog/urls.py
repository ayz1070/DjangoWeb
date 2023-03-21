# urlcof for blog
from django.contrib import admin
from django.urls import path

from . import views

# .index() () 자체는 함수를 호출한다.
# .index 함수를 가져온다...? 의미 공부하자!!
urlpatterns = [
    # blog/(빈 것)
    path('', views.index),
]