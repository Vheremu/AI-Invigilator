from django.contrib import admin
from django.urls import path, include
from . import views,urls
app_name = 'questionbank_app'
urlpatterns = [
    path('index/', views.index.as_view(),name='index'),
    path('list/', views.list,name='list'),
      path('list/<int:pk>',views.QuestionDetailView.as_view(),name='detail'),
    path('create/',views.QuestionCreateView.as_view(),name='create'),
     path('updatequestion/<int:pk>',views.QuestionUpdateView.as_view(),name='update'),
     path('deletequestion/<int:pk>',views.QuestionDeleteView.as_view(),name='delete'),
]