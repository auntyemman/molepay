import json
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .services import UsersService
from .serializers import CreateUserSerializer

class UsersViewSet(viewsets.ViewSet):
    users_service = UsersService()
    
    @action(detail=False, methods=['post'], url_path='register')
    def create_user(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.users_service.create_user(serializer.validated_data)
        return Response({
            "user": CreateUserSerializer(user).data,
            "message": "User created successfully"
        }, status=status.HTTP_201_CREATED)

    # @action(detail=False, methods=['post'])
    # def login(self, request):
    #     serializer = LoginSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     token = self.users_service.login_user(serializer.validated_data)
    #     return Response({"token": token.key}, status=status.HTTP_200_OK)

    # @action(detail=False, methods=['patch'], url_path='profile')
    # def update_profile(self, request):
    #     serializer = UpdateUserProfileSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = self.users_service.update_user_profile(request.user, serializer.validated_data)
    #     return Response({
    #         "user": UpdateUserProfileSerializer(user).data,
    #         "message": "User profile updated successfully"
    #     }, status=status.HTTP_200_OK)
