from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('review', views.review, name='review'),
    path('selection', views.selection, name='selection'),
    path('article', views.article, name='article'),
]