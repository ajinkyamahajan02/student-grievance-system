from django.db import models

# Create your models here.


class GrievanceData(models.Model):
    username = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=254, default=None)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    # image = models.FileField(upload_to='attachments')
    stars = models.IntegerField(default=0)
    is_answered = models.BooleanField(default=False)
    reply = models.CharField(max_length=1000, null=True, blank=True)
