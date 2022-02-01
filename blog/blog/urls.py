from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.posts_views),
    path('post/<int:pk>/', views.post_views, name='post_detail'),
    re_path (r'^tag/(?P<tag_slug>[-\w]+)/$', views.posts_views, name='post_list_by_tag')
]