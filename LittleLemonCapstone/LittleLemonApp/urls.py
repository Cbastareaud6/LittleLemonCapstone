# define URL route for index() view
from django.urls import path
from rest_framework import routers

from .views import MenuView, SingleMenuItemView, home, BookingViewSet



urlpatterns = [

    path('', home, name='home'),
    path('menu/', MenuView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),


]
