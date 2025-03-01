from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class Authenticator():
    def authenticate(self, serializer):       
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"error": "E-mail ou senha inválidos"}, status=400)
            
            if not user.check_password(password):
                return Response({"error": "E-mail ou senha inválidos"}, status=400)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            return Response({
                "access_token": access_token,
                "refresh_token": str(refresh),
            })

        return Response({"error": "E-mail ou senha inválidos"}, status=400)