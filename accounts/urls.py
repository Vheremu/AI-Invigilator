from django.contrib import admin
from django.urls import path , include
from accounts import views
app_name  = 'accounts_app'
urlpatterns = [
    path('',views.user_login,name='index'),
    path('register/',views.register,name='register'),
   path('prompt/',views.prompt,name='prompt'), path('registerstudent/',views.registerstudent,name='registerstudent'), 
   path('registerlecturer/',views.registerlecturer,name='registerlecturer') ,
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('admin/', admin.site.urls),
    ]
