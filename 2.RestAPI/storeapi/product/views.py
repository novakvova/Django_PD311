from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .tokens import CustomTokenObtainPairSerializer
import requests
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from django.core.mail import send_mail


User = get_user_model()
GOOGLE_USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

# Create your views here.
class CategoryViewSet(ModelViewSet):
    print("get data")
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Користувач успішно зареєстрований!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # print("get data", request.data)
        access_token = request.data.get("access_token")
        if not access_token:
            return Response({"detail": "Access token required"}, status=status.HTTP_400_BAD_REQUEST)

        resp = requests.get(GOOGLE_USERINFO_URL, headers={"Authorization": f"Bearer {access_token}"})
        if resp.status_code != 200:
            return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        userinfo = resp.json()
        
        google_id = userinfo.get("sub")               
        email = userinfo.get("email")
        phone = userinfo.get("phone_number")        
        avatar_url = userinfo.get("picture")
        username = userinfo.get("name") or email.split("@")[0]
        isGoogle = True

        if not email:
            return Response({"detail": "Email not provided by Google"}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(email=email, defaults={
            "username": username,
            "isGoogle": isGoogle,
        })


        if phone and not user.phone:
            user.phone = phone
            user.save(update_fields=["phone"])

        refresh = RefreshToken.for_user(user)

        send_mail(
            subject='Тестовий лист',
            message='Це тестовий лист від Django через smtp.ukr.net.',
            from_email='super.novakvova@ukr.net',
            recipient_list=['novakvova@gmail.com'],
            fail_silently=False,
        )

        return Response({
            "id": google_id,
            "email": email,
            "phone": phone,
            "avatar": avatar_url,
            "username": user.username,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        })