
from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.ApiRoot.as_view()),
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user'),
    path('informations/', views.InformationList.as_view(), name='informations'),

]
