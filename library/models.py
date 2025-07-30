from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    content = models.TextField()
    publicated_date = models.DateTimeField()
    
    def __str__(self):
        return f'책 제목 : {self.title}\
            저자 : {self.author}\
            내용 : {self.content}\
            발행일 : {self.publicated_date}'
            
    def get_absolute_url(self):
        return f'/library/{self.pk}/'  # return url 지정
        # return reverse("model_detail", kwargs={"pk": self.pk})
    