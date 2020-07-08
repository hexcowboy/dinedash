"""
Url paths for the Menu app
These endpoints are accessed from <domain>/menus/<pattern>
"""
from django.urls import path

from . import views

app_name = "menu"
urlpatterns = [
    path("", views.MenuList.as_view(), name="list"),
    path("create", views.MenuCreate.as_view(), name="create"),
    path("<pk>", views.MenuDetail.as_view(), name="detail"),
    path("<pk>/delete", views.MenuDelete.as_view(), name="delete"),
    path("<pk>/update", views.MenuUpdate.as_view(), name="update"),
    path("<str:menu_pk>/category/create", views.MenuCategoryCreate.as_view(), name='create_category'),
    path("<str:menu_pk>/category/<pk>/delete", views.MenuCategoryDelete.as_view(), name='delete_category'),
    path("<str:menu_pk>/category/<pk>/update", views.MenuCategoryUpdate.as_view(), name='update_category'),
]
