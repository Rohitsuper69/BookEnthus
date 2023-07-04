from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.home,name='home'),
    path('bookreview',views.bookReview_view,name='bookreview'),
    path('review',views.review,name='review'),
    path("delete_review/<int:pk>",views.deletereview,name="deletereview"),
    path('todo',views.todo_view,name='todo'),
    path("toread",views.toread,name="toread"),
    path("delete-todo/<int:pk>",views.to_delete,name="delete-todo"),
    path("books",views.books,name="books"),
    path('dict',views.dict,name="dict"),
    path('profile',views.profile,name='profile'),
    path('cprofile',views.cprofile,name='create-profile'),
    path('online_reviews',views.online_reviews, name='online-reviews'),
]
