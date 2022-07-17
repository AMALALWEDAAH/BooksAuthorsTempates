from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_book',views.add_book),
    path('view_book/<int:id>',views.view_book),
    path('authors',views.authors),
    path('add_author',views.add_author),
    path('view_author/<int:id>',views.view_author),
    path('append_author/<int:id>',views.append_author)
]