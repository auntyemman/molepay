from django.db import models
from uuid import uuid4

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, db_index=True, auto_created=True)
    email = models.EmailField(unique=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=250, null=False)
    phone = models.CharField(max_length=15)
    picture = models.URLField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} ({self.email})"