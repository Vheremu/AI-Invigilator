from django.contrib import admin
from django.urls import path, include
from . import views,urls
app_name = 'students_app'
urlpatterns = [
    path('',views.register,name='register'),
    path('mysittings',views.mySittings,name='mysittings'),
    path('<int:pk>',views.sittingdetails,name='sittingdetails'),
    path('deletesittingrequest/<int:pk>',views.deletesittingrequest,name='deletesittingrequest')

]
