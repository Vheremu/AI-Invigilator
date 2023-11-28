from django.contrib import admin
from django.urls import path, include
from . import views,urls
app_name = 'exams_app'
urlpatterns = [
    path('index/', views.index.as_view(),name='index'),
    path('addexam/', views.AddExam_view,name='addexam'),
    path('list/',views.listExams,name='list'),
    path('list/<int:pk>',views.ExamDetailView.as_view(),name='detail'),
    path('questionDetail/<int:pk>',views.QuestionDetailView.as_view(),name='questiondetail'),
    path('create/',views.ExamCreateView.as_view(),name='create'),
    path('createquestion/',views.QuestionCreateView.as_view(),name='createquestion'),
    path('update/<int:pk>',views.ExamUpdateView.as_view(),name='update'),
    path('updatequestion/<int:pk>',views.QuestionUpdateView.as_view(),name='updatequestion'),
    path('delete/<int:pk>',views.ExamDeleteView.as_view(),name='delete'),
    path('deletequestion/<int:pk>',views.QuestionDeleteView.as_view(),name='deletequestion'),

]
# urlpatterns = [
#     path('',views.index.as_view(),name='index'),
#     path('list/',views.ListGroups.as_view(),name='list'),
#     path('list/<int:pk>',views.SingleGroup.as_view(),name='detail'),
#     path('create/',views.CreateGroup.as_view(),name='create'),
#     path('createmember/',views.CreateGroupMember.as_view(),name='createmember'),
#     path('update/<int:pk>',views.GroupUpdateView.as_view(),name='update'),
#     path('delete/<int:pk>',views.GroupDeleteView.as_view(),name='delete'),
# ]
