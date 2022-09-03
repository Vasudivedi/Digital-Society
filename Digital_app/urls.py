from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("register_page/", register_page, name='register_page'),
    path("login/", login, name='login'),
    path("profile_page/", profile_page, name='profile_page'),
    path("handle_login/", handle_login, name="handle_login"),
    path("register/", register, name="register"),
    path("profile_update/", profile_update, name='profile_update'),
    path("logout/",logout,name ='logout'),
    path("",home_page,name= 'home_page'),
    path("contact_page/",contact_page,name ='contact_page'),
    path('mail_send/', mail_send, name='mail_send'),
    path('about_us/', about_us, name='about_us'),
   ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)