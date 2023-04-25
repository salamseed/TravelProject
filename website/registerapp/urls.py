from . import views
from django.urls import path
urlpatterns = [
    path('register',views.displayreg,name='displayreg'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]