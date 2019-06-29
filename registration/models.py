from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteUser(User):
    def __str__(self):
        super().__str__(self)

