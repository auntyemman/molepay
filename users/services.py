from .repository import UsersRepository
from .models import User
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from core.helper.exceptions import AlreadyExistsException
from django.contrib.auth.hashers import make_password, check_password

import logging

logger = logging.getLogger('molepay')
class UsersService:
    def __init__(self):
        self.user_repository = UsersRepository()

    def create_user(self, user_data: dict) -> User:
        if self.user_repository.get_one_by_email(email=user_data['email']):
            raise AlreadyExistsException
        try:
            # Hash the password before creating the user
            user_data['password'] = make_password(user_data['password'])
            instance = User(**user_data)  # Create a User model instance
            new_user = self.user_repository.create(instance)
        except Exception as e:
            raise ValidationError(str(e))
        else:
            return new_user
    def login(self, user_data: dict) -> User:
        user = self.user_repository.get_one_by_email(email=user_data['email'])
        if user and check_password(user_data['password'], user.password):
            return user
        else:
            raise AuthenticationFailed('Invalid email or password.')
    

    def update_user(self, user: User) -> User:
        return self.user_repository.update(user)

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_one(user_id)

    def delete_user(self, user_id: int) -> None:
        return self.user_repository.delete(user_id)

    def bulk_create_users(self, users_data: list[dict]):
        with self.user_repository.transaction():
            for user_data in users_data:
                user = User(**user_data)
                self.user_repository.create(user)
