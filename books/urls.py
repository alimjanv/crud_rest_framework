from .views import BooksAPIView, AuthorRetrieveAPIView, SigninView, SignUpView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('books', BooksAPIView.as_view(), name='booksold-list-create'),
    path('books/<int:pk>', BooksAPIView.as_view(), name='delete-update'),
    path('authors', AuthorRetrieveAPIView.as_view(), name='author-create'),
    path('authors/<int:pk>', AuthorRetrieveAPIView.as_view(), name='author-detail'),
    path('token', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('signin', SigninView.as_view(), name='signin'),

]











