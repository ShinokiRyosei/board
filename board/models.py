from django.db import models
from django.contrib.auth.models import User
# Create your models here.
user = User

class Post(models.Model):
    content = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(user)

    def __str__(self):
        return self.content

