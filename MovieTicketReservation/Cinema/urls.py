from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns =[
    path("", views.registration, name="registration"),
    path("Home/", views.home, name="home"),
    path("login/",views.user_login, name="login"),
    path("<int:key>/",views.details,name='details'),
    path("<int:key>/<int:shows>/", views.seat, name="seat"),
    path("payment/<int:key>/<int:shows>/<int:seats>/",views.payment, name="payment"),
    path("ticket/<int:key>/<int:shows>/<int:seats>/", views.ticket, name="ticket"),


    #path("admin/", views.admin, name="admin")

] 
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:

   #  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
