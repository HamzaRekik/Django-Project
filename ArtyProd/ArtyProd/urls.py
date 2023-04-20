from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("team/", include("team.urls")),
    path("login/", views.login_view, name="login"),
    path("signin/", views.signin_view, name="signin"),
    path("logout/", views.logout_view, name="logout"),
    path("contact_us/", views.contact, name="contact"),
    path("services/", include("services.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("blogger/", views.blog_view, name="blog"),
    path("article/<str:pk>", views.article_view, name="article"),
    path("", views.main, name="main"),
]
