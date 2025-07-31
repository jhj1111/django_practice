from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: # class 설명
        model = Post
        fields = ['title', 'content', 'uploaded_image']   # 속성값 입력, template, 오타 조심