from django.urls import path
from myblog import views

app_name = 'myblog'
urlpatterns=[
    path('',views.index,name='index'),
    path('add_new_blog_ajax/',views.add_new_blog_ajax,name='add_new_blog_ajax'),
    path('add_likes_ajax/',views.add_likes_ajax,name='add_likes_ajax'),
    path('delete_blog_ajax/',views.delete_blog_ajax,name='delete_blog_ajax')
]