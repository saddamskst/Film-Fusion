# from django.urls import url
# from django.conf import settings,urls
# from django.views.static import serve 

from django.contrib import admin
from django.urls import path
from .views import *
# from django.views.defaults import page_not_found

urlpatterns = [
    # urls(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # urls(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),
    path('',home),
    path('detail',detail),
    path('movie-list',movielist),
    path('login',login),
    path('logout',logout),
    path('signup',signup),
    path('team',team),
    path('contact',contact),
    
   # path('login',contact),

]

handler404 = 'FilmFusion.views.error_page'
