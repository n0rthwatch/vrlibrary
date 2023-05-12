from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('books/', BookListView.as_view(), name='books'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
    path('news/', news, name='news'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),

    path('login/', sign_in, name='login'),
    path('logout/', sign_out, name='logout'),
    path('register/', sign_up, name='register'),
    path('profile/', profile, name='profile'),
    path('remove_favorite/<int:book_id>', remove_favorite, name='remove_favorite'),
    path('add_favorite/<int:book_id>', add_favorite, name='add_favorite'),
]
