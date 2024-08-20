# from contextlib import contextmanager
# from django.db import transaction
# from django.db.models import Model
# from typing import List, Optional
# from .abstract_base_repository import AbstractBaseRepository, T

# class BaseRepository(AbstractBaseRepository[T]):

#     def __init__(self, model: Model):
#         self.model = model

#     async def create(self, obj: Model) -> Model:
#         #obj.save()
#         return await self.model.save(obj)

#     async def update(self, obj: T) -> T:
#         # obj.save()
#         # return obj
#         return await self.model.save(obj)

#     def get_one(self, id: int) -> Optional[T]:
#         try:
#             return self.model.objects.get(id=id)
#         except self.model.DoesNotExist:
#             return None

#     def get_many(self, filters: dict = {}) -> List[T]:
#         return list(self.model.objects.filter(**filters))

#     def delete(self, id: int) -> None:
#         self.model.objects.filter(id=id).delete()

#     @contextmanager
#     def transaction(self):
#         """Context manager for handling transactions."""
#         with transaction.atomic():
#             yield
