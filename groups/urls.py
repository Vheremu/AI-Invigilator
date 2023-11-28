from django.contrib import admin
from django.urls import path, include
from . import views,urls
app_name = 'groups_app'
urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('addmember/',views.AddMember,name='addmember'),
    path('list/',views.listGroups,name='list'),
    path('list/<int:pk>',views.SingleGroup.as_view(),name='detail'),
    path('memberdetail/<int:pk>',views.MemberDetailView.as_view(),name='memberdetail'),
    path('memberrequestdetail/<int:pk>',views.MemberRequestDetailView.as_view(),name='memberrequestdetail'),
    path('create/',views.creategroup,name='create'),
    path('createmember/',views.CreateGroupMember.as_view(),name='createmember'),
    path('update/<int:pk>',views.GroupUpdateView.as_view(),name='update'),
    path('updatemember/<int:pk>',views.MemberUpdateView.as_view(),name='updatemember'),
    path('delete/<int:pk>',views.GroupDeleteView.as_view(),name='delete'),
    path('deletemember/',views.MemberDeleteView,name='deletemember'),
    path('deletememberrequest/',views.MemberRequestDeleteView,name='deletememberrequest'),
]
