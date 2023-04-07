# define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import MenuView, SingleMenuItemView, home

urlpatterns = [

    path('', home, name='home'),
    path('menu/', MenuView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)

]
