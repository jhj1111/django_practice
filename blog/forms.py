from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    uploaded_file = forms.FileField(label='uploaded_file',
                                    required=False,
                                    widget=forms.FileInput(attrs={'class' : 'document_form'}),  # css class='document_from'
                                    )
    class Meta: # class 설명
        model = Post
        fields = ['title', 'author', 'category', 'content', 'uploaded_image', 'uploaded_file']   # 속성값 입력, template, 오타 조심