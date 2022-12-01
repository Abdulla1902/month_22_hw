from django.db import models

# Create your models here.

POST_TYPE_CHOICES = (
    (1, 'Image'),
    (2, 'Video'),
    (3, 'Audio'),
    (4, 'Music')
)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    stars = models.IntegerField(null=True)
    type = models.IntegerField(choices=POST_TYPE_CHOICES, null=True)