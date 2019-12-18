import uuid
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    created_time = models.DateTimeField(default=timezone.now, db_index=True)
    email = models.EmailField()
    used = models.BooleanField(default=False)
    creator = models.ForeignKey(User, related_name='created_invitations', \
        on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.email
