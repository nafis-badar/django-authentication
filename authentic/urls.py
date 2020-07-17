from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.loginuser,name="login"),
    path('logout/',views.logoutuser,name="logout"),
]