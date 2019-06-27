from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField('date_published')
    date_updated = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.title} {self.date_created}'
