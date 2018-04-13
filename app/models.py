from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tweet(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)


class Message(models.Model):
    to_user = models.ForeignKey(User, related_name='message_to')
    from_user = models.ForeignKey(User, related_name='message_from')
    content = models.TextField()
    already_read = models.BooleanField(default=False)
    sent_date = models.DateTimeField(auto_now_add=True)
