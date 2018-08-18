from django.db import models
from django.conf import settings
# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField(max_length=256)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)

