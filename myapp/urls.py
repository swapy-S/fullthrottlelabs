from django.urls import path, re_path
from . import views


app_name = "myapp"
urlpatterns = [
    path("api/", views.ArticalAPIView.as_view(), name="api"),
    path("", views.home, name="home"),
    path("create_user/", views.UserCreateView.as_view(), name="create_user"),
    path("create_activity/", views.ActivityCreateView.as_view(), name="create_activity"),
]
