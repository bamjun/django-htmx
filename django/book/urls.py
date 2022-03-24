from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.index, name='index'),
    path('htmx/book-form/', views.create_book_form, name='book-form'),
    path('htmx/book/<pk>/', views.detail_book, name='detail-form'),
    path('htmx/book/<pk>/update', views.update_book, name='update-form'),
    path('htmx/book/<pk>/delete', views.delete_book, name='delete-form'),
]
