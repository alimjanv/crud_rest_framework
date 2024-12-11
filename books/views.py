from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
# from customer.models.customer import Customer
# from customer.serializers.customer import CustomerSerializer
# from ..order.models.order import Order
# from ..order.models.order_item import OrderItem
from .serializers.author import AuthorSerializers
from .serializers.book import BookSerializers
from .models.author import Author
from .models.book import Book
# from ..order.serializers.order import OrderSerializers
# from ..order.serializers.order_item import OrderItemSerializers
from .serializers.signup import SignupSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken




class BooksAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, pk=None):
            if pk:
                book = get_object_or_404(Book, pk=pk)
                serializer = BookSerializers(book)
                return Response(serializer.data)
            else:
                books = Book.objects.all()
                serializer = BookSerializers(books, many=True)
                return Response(serializer.data)

    def post(self, request):

        request.data['author'] = request.user.id
        serializer = BookSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
            book = get_object_or_404(Book, pk=pk)
            serializer = BookSerializers(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
            book = get_object_or_404(Book, pk=pk)
            print(request.user)

            if book.author != request.user:
                return Response({"detail": "Siz faqat o'z kitoblaringizni o'chira olasiz."},
                                status=status.HTTP_403_FORBIDDEN)

            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



class AuthorRetrieveAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializers(author)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializers(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Foydalanuvchi ro'yxatdan o'tdi!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Tizimga muvaffaqiyatli kirdingiz!"
            })
        return Response({"error": "Noto'g'ri username yoki parol"}, status=status.HTTP_401_UNAUTHORIZED)




