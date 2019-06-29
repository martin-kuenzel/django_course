from django.db import models
from django.utils import timezone
import datetime

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} {self.date_created}'

    def was_created_recently(self):
        return timezone.now() >= self.date_created >= timezone.now() - datetime.timedelta(days=1)

    was_created_recently.admin_order_field = 'date_created'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently'
    
    def was_updated_recently(self):
        return self.date_updated >= timezone.now() - datetime.timedelta(days=1)

    was_updated_recently.admin_order_field = 'date_updated'
    was_updated_recently.boolean = True
    was_updated_recently.short_description = 'Updated recently'