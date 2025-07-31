from django.contrib.auth.models import User
from django.db import models
import os
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_created=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    uploaded_image = models.ImageField(upload_to='images/', null=True)
    uploaded_file = models.FileField(upload_to='files/', null=True)
    
    def __str__(self):
        image_path = self.get_image_url()
        file_name = self.get_file_name()
        
        
        list_str = ['제목', '내용', '생성일', '변경일', '이미지 경로', '파일 경로']
        list_var = [self.title, self.content, self.create_date, self.updated_date, image_path, file_name]
        
        # return f'post title : {self.title}\ncontent : {self.content} updated : {self.updated_date}'
        return '\n'.join([f'{i} : {j}' for i,j in zip(list_str, list_var)])
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'  # return url 지정
        # return reverse("model_detail", kwargs={"pk": self.pk})
    
    def get_file_name(self):
        try : file_path = os.path.basename(self.uploaded_file.name)
        except (ValueError, TypeError) : file_path = None
        
        return file_path
    
    def get_image_url(self):
        try : image_url = self.uploaded_image.url
        except ValueError : image_url = None
        
        return image_url