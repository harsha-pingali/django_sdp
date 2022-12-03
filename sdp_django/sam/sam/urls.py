from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',include('app1.urls')),
    path('admin/', admin.site.urls),
    #path('',include('app1.urls')),
    #path('',include('app2.urls'))
]
