from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="rooms"),
    path('profile/<str:pk>/', views.userprofile, name="profile"),
    path('create-room/', views.createroom, name="create-room"),
    path('update-room/<str:pk>/', views.updateroom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteroom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deletemessage, name="delete-message"),
    path('update-user/', views.updateuser, name="update-user"),
    path('search/', views.custom_search, name="search"),
    path('broadcast', views.broadcast_message, name="broadcast_message"),
    path('topic', views.topicpage, name="topic"),
    path('activity', views.activitypage, name="activity"),
    

]
