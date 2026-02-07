import json
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status


class CsrfView(APIView):
    permission_classes = [AllowAny]

    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        return Response({"csrfToken": get_token(request)})




class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request)
        #works for JSON bodies

        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "username or password is required"}, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({"error": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user) #create session + sets cookie

        return Response({
            "message": "Login success",
        })


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response({"message": "Logout success"})


