from django.urls import path
#from django.conf import settings
#from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    #path('welcome/', views.welcome, name='welcome'),
    path('newuser/', views.register, name='registration'),
    path('verify/',views.verify,name='verify'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile),
    path('logout/',views.user_logout,name='logout')
   # path('home/',views.home,name='home')

]
#urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
