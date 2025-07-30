from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    
    def __str__(self):
        return f'post title : {self.title}\ncontent : {self.content}'
    
    
        