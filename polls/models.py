from django.db import models
from datetime import datetime

class Poll(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField('date_published')

    def __str__(self):
        return f'{self.title}'

    def was_published_recently(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=1)

class Option(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} ({self.votes} votes)'
