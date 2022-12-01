from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    #path('welcome/', views.welcome, name='welcome'),
    path('newuser/', views.register, name='registration'),
   # path('home/',views.home,name='home')

]
