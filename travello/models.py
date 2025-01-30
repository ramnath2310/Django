from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = RichTextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Comment(models.Model):  
    destination = models.ForeignKey(Destination, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"

    def like_count(self):
        return self.likes.count()

    def dislike_count(self):
        return self.dislikes.count()
