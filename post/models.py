from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=300, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class CreatePost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)