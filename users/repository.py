from contextlib import contextmanager
from django.db import transaction
from typing import List, Optional
from .models import User

class UsersRepository:
    def __init__(self):
        self.users = User

    def create(self, user: User) -> User:
        user.save()  # Save the model instance
        return user

    def update(self, user: User) -> User:
        user.save()  # Save changes
        return user

    def get_one(self, id: int) -> Optional[User]:
        try:
            return self.users.objects.get(id=id)
        except self.users.DoesNotExist:
            return None
    def get_one_by_email(self, email: str) -> Optional[User]:
        try:
            return self.users.objects.get(email=email)
        except self.users.DoesNotExist:
            return None

    def get_many(self, filters: dict = {}) -> List[User]:
        return list(self.users.objects.filter(**filters))

    def delete(self, id: int) -> None:
        self.users.objects.filter(id=id).delete()

    @contextmanager
    def transaction(self):
        """Context manager for handling transactions."""
        with transaction.atomic():
            yield
