import datetime
from django.db import models
from django.utils import timezone

class Poll(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField('date_published')

    def __str__(self):
        return f'{self.title}'

    def was_published_recently(self):
        return timezone.now() >= self.date_created >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'date_created'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'

class Option(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} ({self.votes} votes)'
