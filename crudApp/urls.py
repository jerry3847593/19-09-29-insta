from django.urls import path
from . import views

urlpatterns = [
    # path('home/',home,name='home'),
    #path('create_post/',create_post,name='create_post'),
    #path('edit_post/<int:post_pk>',edit_post,name='edit_post'),
    #path('delete_post/<int:post_pk>',delete_post,name='delete_post'),
    path('home/', views.Home.as_view(), name='home'),
    path('create_post', views.Create_post.as_view(), name="create_post"),
    path('edit_post/<int:pk>', views.Edit_post.as_view(), name='edit_post'),
    path('delete_post/<int:pk>', views.Delete_post.as_view(), name="delete_post"),
    path('detail_post/<int:pk>', views.Detail_post.as_view(), name='detail_post'),
]