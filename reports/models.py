from django.db import models
import uuid
from django.utils.timezone import now
from datetime import date


class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    note = models.TextField(default='Note here')
    created_at = models.DateField(default=date.today)
    modified = models.DateField(default=now)

    def __str__(self):
        return f'{self.title} with the note {self.note}'
