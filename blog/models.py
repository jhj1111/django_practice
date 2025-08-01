from django.contrib.auth.models import User
from django.db import models
import os
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)    # 중복 방지, 주소 이용
    
    def __str__(self):
        return super().__str__()
    
    def get_absolute_url(self):
        return f'/blog/categories/{self.slug}/'  # return url 지정
    


class Post(models.Model):
    author = models.ForeignKey(User, 
                            #    on_delete=models.CASCADE,    # User가 없다면 post 자체를 없애겠다(user 삭제 -> user가 쓴 글 같이 삭제)
                               on_delete=models.SET_NULL,    # User가 없어도 post는 유지
                               null=True,
                               )  
    
    category = models.ForeignKey(Category, 
                            #    on_delete=models.CASCADE,    # User가 없다면 post 자체를 없애겠다(user 삭제 -> user가 쓴 글 같이 삭제)
                               on_delete=models.SET_NULL,    # User가 없어도 post는 유지
                               null=True,
                               blank=True,
                               )  
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    uploaded_image = models.ImageField(upload_to='images/', null=True)
    uploaded_file = models.FileField(upload_to='files/', null=True)
    
    def __str__(self):
        image_path = self.get_image_url()
        file_name = self.get_file_name()
        
        
        list_str = ['제목', '작성자', '내용', '카테고리','생성일', '변경일', '이미지 경로', '파일 경로']
        list_var = [self.title, self.author, self.content, self.category, self.create_date, self.updated_date, image_path, file_name]
        
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