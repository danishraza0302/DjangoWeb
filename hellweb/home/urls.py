from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "SMARTEEN CLOTH Admin"
admin.site.site_title = "SMARTEEN CLOTHS Admin Portal"
admin.site.index_title = "Welcome to SMARTEEN MANSWEAR"

urlpatterns = [
    path("",views.index,name='home'),
    path("help",views.help,name='help'),
    path("sell",views.sell,name='sell'),
    path("club",views.club,name='club'),
]