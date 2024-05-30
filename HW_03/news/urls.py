from django.urls import path
from .views import PostList, IdPostList, AuthorList

urlpatterns = [
    path('', PostList.as_view()),
    path('author/', AuthorList.as_view()),
    path('<int:pk>/новости', IdPostList.as_view(), name='new'),
]