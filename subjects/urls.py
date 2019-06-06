
from django.urls import path 
from . import views

urlpatterns = [
    path('new_subject/',views.new_subeject,name = 'new_subject'),
    path('create_subject/',views.create_subject,name='create_subject'),
    path('<int:id>/',views.show_subject,name='show_subject'),
    path('update_subject/<int:id>/',views.update_subject,name='update_subject'),
    path('delete_subject/<int:id>/',views.delete_subject,name='delete_subject'),
    
    path('<int:id>/new_post/',views.new_post,name = 'new_post'),
    path('<int:id>/create_post/',views.create_post,name='create_post'),
    path('<int:id>/update_post/',views.update_post,name='update_post'),
    path('<int:id>/delete_post/',views.delete_post,name='delete_post'),
    
    
    path('<int:id>/post/create_like/',views.create_like,name='create_like'),
    path('<int:id>/post/create_dislike/',views.create_dislike,name='create_dislike'),
    path('<int:id>/post/likes_check/',views.likes_check,name='likes_check'),
    path('post/like_list/',views.like_list,name='like_list'),
]
