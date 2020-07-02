from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.MenuList.as_view(), name='list'),
    path('<pk>', views.MenuDetail.as_view(), name='detail'),
]
