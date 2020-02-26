from django.urls import path, include
from . import views

app_name = 'friends'
urlpatterns = [
    path('', views.friendList, name='friend-list'),
    path('friend/<int:id>', views.friendView, name='friend-view'),
    path('createfriend/', views.createFriend, name='create-friend'), 
    path('editfriend/<int:id>', views.editFriend, name='edit-friend'), 
    path('deletefriend/<int:id>', views.deleteFriend, name='delete-friend'),
    path('account/', include('django.contrib.auth.urls')),
]
