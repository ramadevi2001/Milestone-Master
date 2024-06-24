from django.db import models

# Create your models here.
import uuid

class User(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=50, null=False)
    LastName = models.CharField(max_length=50, null=False)
    Email = models.EmailField(max_length=50, unique=True, null=False)
    Password = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.Email




