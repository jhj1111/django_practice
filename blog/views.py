from django.shortcuts import render
from django.shortcuts import redirect   # 주소 변경
from .models import *
from .forms import *
from django.http import HttpResponse
import os
from django.conf import settings
# from django_project_practice import settings


# Create your views here.
def index(request):
    posts_total_list = Post.objects.all().order_by('-pk') # db SELECT * FROM POST ... ASC
    # posts_total_list = Post.objects.all() # db SELECT * FROM POST
    category_total_list = Category.objects.all() # db SELECT * FROM POST ... ASC
    comments = Comment.objects.all()
    
    
    return render(request, 
                  template_name='blog/index.html',
                  context={'posts':posts_total_list,
                            'categories' : category_total_list,
                            'comments' : comments,
                            }
                  )
    
def detail(request, pk, commentform=None):
    category_total_list = Category.objects.all() # db SELECT * FROM POST ... ASC
    post_pk = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post_pk).order_by('created_date')
    commentform = CommentForm() if commentform is None else commentform
    
    return render(request,
                  template_name='blog/detail.html',
                  context={'post_pk':post_pk,
                        'categories' : category_total_list,
                        'comments' : comments,
                        'commentform' : commentform,
                        }
                  )
    
def categories(request, slug):
    category_total_list = Category.objects.all() # db SELECT * FROM POST ... ASC
    if slug=='0':
        category_posts = Post.objects.filter(category=None)
        posts_category = ''
    else :
        posts_category = Category.objects.get(slug=slug)
        category_posts = Post.objects.filter(category=posts_category)
    
    return render(request,
                  template_name='blog/categories.html',
                  context={'category_posts':category_posts,
                           'category' : posts_category,
                           'categories' : category_total_list,
                            },
                  )
    
def create(request, pk=None):
    state = 'create' if pk is None else 'update'
    category_total_list = Category.objects.all() # db SELECT * FROM POST ... ASC    
    posts_pk_list = Post.objects.get(pk=pk) if state=='update' else None
    
    if request.method == 'POST':    # 제출 버튼 
        postform = PostForm(request.POST, request.FILES) if state=='create' else PostForm(request.POST, request.FILES, instance=posts_pk_list)
            
        
        if postform.is_valid: # 작성 도중 제출 버튼 누른경우
            temp_post = postform.save(commit=False) # 저장 메소드를 가진 객체 반환
            
            temp_post.title = temp_post.title if '--' not in temp_post.title \
                else temp_post.title+' injection' # 제출 시 추가 동작 실행
            temp_post.save() # 정상적인 경우 -> DB 저장
            
            return redirect('index')    # return redirect('/blog/')
        
    else : # GET
        postform = PostForm() if state=='create' else PostForm(instance=posts_pk_list)
    
    return render(request,
                  template_name='blog/postform.html',
                  context={'postform' : postform,
                           'categories' : category_total_list,
                           },
                  )

def createfake(request, pk=None):
    post = Post()
    post.title = ' fake post title'
    post.content = 'fake post content'
    post.save()
    
    return redirect('/blog/')
    # return redirect('index')

def file_download(request):
    path = request.GET['path']
    file_path = os.path.join(settings.MEDIA_ROOT, path)
 
    if os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/octet-stream; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        message = '알 수 없는 오류가 발행하였습니다.'
        return HttpResponse("<script>alert('"+ message +"');history.back()'</script>")
    
def delete(request, pk):
    posts_pk_list = Post.objects.get(pk=pk)
    posts_pk_list.delete()
    
    return redirect('index')    # return redirect('/blog/')


def comment_create(request, pk, id=None):
    state = 'create' if id is None else 'update'
    post_pk = Post.objects.get(pk=pk)
    comment = Comment.objects.get(pk=id) if state=='update' else None
    commentform = CommentForm(request.POST) if state=='create' else CommentForm(request.POST, instance=comment)
    
    if request.method == 'POST' and commentform.is_valid(): # create
        temp_comment = commentform.save(commit=False)
        temp_comment.post = post_pk
        temp_comment.save()
        return redirect(post_pk.get_absolute_url())
    else:   # update
        commentform = CommentForm(instance=comment)
        commentform.id = comment.id
        commentform.pk = comment.pk
        commentform.created_date = comment.created_date
        commentform.updated_date = comment.updated_date
        
        comment.delete()
        return detail(request, post_pk.pk, commentform)
        
    return render(request,
                  template_name='blog/detail.html',
                  context={'commentform':commentform,
                           })
    
def comment_delete(request, pk, id):
    post_pk = Post.objects.get(pk=pk)
    comment = Comment.objects.get(pk=id)
    comment.delete()
    
    return redirect(f'/blog/{comment.pk}')
