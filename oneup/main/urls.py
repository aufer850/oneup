from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('review', views.review, name='review'),
    path('article', views.article, name='article'),
    path('selection', views.selection, name='selection'),
    path('<int:article_id>', views.articlewindow, name='articlewindow'),
    path('<int:article_id>/like/', views.like_article, name='like_article'),
    path('<int:article_id>/dislike/', views.dislike_article, name='dislike_article'),
    path('<int:article_id>/comment/', views.comment, name='comment'),
]