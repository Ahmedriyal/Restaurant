from django.urls import path, include

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path("signup", views.signup, name="signup"),
	path("signin", views.signin, name="signin"),
	path("logout", views.logout, name="logout"),


]