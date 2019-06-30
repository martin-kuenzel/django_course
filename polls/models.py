import datetime
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Poll(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.title}'

    def was_published_recently(self):
        return timezone.now() >= self.date_created >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'date_created'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'

class OptionSet(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)
    #requires = models.ManyToManyField(Option,default=None)
    #constraints = models.ManyToManyField(Option,default=None)

    def __str__(self):
        return f'{self.title}'

class Option(models.Model):
    # poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    optionset = models.ForeignKey(OptionSet,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} ({self.votes} votes)'
