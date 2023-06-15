from django.contrib import admin
from django.urls import path
from django.conf.urls.static import settings
from django.conf.urls.static import static

from  woow.views import *

urlpatterns = [

    path('', Index, name='home'),
    path('admin/', admin.site.urls),


    # path('', user_page, name = 'home'),
    # path('user/', Post_today, name = 'posts'),
    # path('<int:pk>/',   PostDetailView.as_view(), name='post')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



password = '1234'
login = 'second'