from django.contrib import admin
from django.urls import path, include
from sittings import views
app_name = 'sittings_app'
urlpatterns = [
    path('', views.index.as_view(),name='index'),
    path('list/',views.listSitting,name='list'),
    path('list/<int:pk>',views.SittingDetailView.as_view(),name='detail'),
    path('update/<int:pk>',views.SittingUpdateView.as_view(),name='update'),
    path('updatecandidate/<int:pk>',views.CandidateUpdateView.as_view(),name='updatecandidate'),
    path('delete/<int:pk>',views.SittingDeleteView.as_view(),name='delete'),
    path('deletecandidate/<int:pk>',views.CandidateDeleteView.as_view(),name='deletecandidate'),
    path('deletecandidaterequest/<int:pk>',views.CandidateRequestDeleteView.as_view(),name='deletecandidaterequest'),
    path('create/',views.SittingCreateView.as_view(),name='create'),
    path('createcandidate/',views.CandidateCreateView.as_view(),name='createcandidate'),
    path('addcandidate/',views.AddCandidateView,name='addcandidate'),
    path('candidateDetail/<int:pk>',views.CandidateDetailView.as_view(),name='candidatedetail'),
    path('candidaterequestDetail/<int:pk>',views.CandidateRequestDetailView.as_view(),name='candidaterequestdetail'),
]
