from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True) # Can be left blank...
    event_date = models.DateTimeField(verbose_name='Date of the event')
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Cascade: Delete all from user

    class Meta:
        db_table = 'event'

    def __str__(self):
        return self.title