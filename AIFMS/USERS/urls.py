from django.contrib import admin
from django.urls import path
from USERS import views
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.user_login, name="login"),
    path("user_settings", views.userSettings, name="user_settings"),
    path("update_theme", views.updateTheme, name="update_theme"),
    path("profile", views.profile_page_view, name="profile"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path(
        "logout",
        CustomLogoutView.as_view(),
        name="logout",
    ),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
