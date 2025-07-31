from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now=True, null=True)
    
    
    def __str__(self):
        list_str = ['제목', '내용', '생성일', '변경일']
        list_var = [self.title, self.content, self.create_date, self.updated_date]
        
        # return f'post title : {self.title}\ncontent : {self.content} updated : {self.updated_date}'
        return '\n'.join([f'{i} : {j}' for i,j in zip(list_str, list_var)])
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'  # return url 지정
        # return reverse("model_detail", kwargs={"pk": self.pk})
    
        