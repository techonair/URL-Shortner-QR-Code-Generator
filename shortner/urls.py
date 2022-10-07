from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:shortned_part>/", views.redirect_url_view, name='redirect'),
]