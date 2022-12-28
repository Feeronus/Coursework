from django.urls import include, path
from . import views


app_name = 'coupons'
urlpatterns = [
    path(r'^apply', views.coupon_apply, name='apply'),
]