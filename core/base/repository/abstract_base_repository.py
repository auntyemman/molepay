from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

# Define a type variable for models
T = TypeVar('T')

class AbstractBaseRepository(ABC, Generic[T]):

    @abstractmethod
    def create(self, obj: T) -> T:
        """Create a new object in the database."""
        pass

    @abstractmethod
    def update(self, obj: T) -> T:
        """Update an existing object in the database."""
        pass

    @abstractmethod
    def get_one(self, id: int) -> Optional[T]:
        """Retrieve a single object by its ID."""
        pass

    @abstractmethod
    def get_many(self, filters: dict = {}) -> List[T]:
        """Retrieve multiple objects, optionally filtered by certain criteria."""
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """Delete an object by its ID."""
        pass

    @abstractmethod
    def transaction(self):
        """Context manager for handling transactions."""
        pass
