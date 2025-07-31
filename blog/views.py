from django.shortcuts import render
from django.shortcuts import redirect   # 주소 변경
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    # posts_total_list = Post.objects.all() # db SELECT * FROM POST
    posts_total_list = Post.objects.all().order_by('-pk') # db SELECT * FROM POST ... ASC
    
    return render(request, 
                  template_name='blog/index.html',
                  context={'posts':posts_total_list},
                  )
    
def detail(request, pk):
    posts_page_list = Post.objects.get(pk=pk)
    
    return render(request,
                  template_name='blog/detail.html',
                  context={'post_page' : posts_page_list})
    
def create(request):
    if request.method == 'POST':    # 제출 버튼 
        postform = PostForm(request.POST, request.FILES)
        
        if postform.is_valid(): # 작성 도중 제출 버튼 누른경우
            temp_post = postform.save(commit=False) # 저장 메소드를 가진 객체 반환
            if '--' not in temp_post.title:
                temp_post.save()
                return redirect('/blog/')
            
            temp_post.title += ' injection' # 제출 시 추가 동작 실행
            # temp_post.author = request.user
            temp_post.save() # 정상적인 경우 -> DB 저장
            
            return redirect('/blog/')  # blog로 돌아감
        
    else : # GET
        postform = PostForm()
    
    return render(request,
                  template_name='blog/postform.html',
                  context={'postform' : postform},
                  )

def createfake(request):
    post = Post()
    post.title = ' fake post title'
    post.content = 'fake post content'
    post.save()
    
    return redirect('/blog/')
    # return redirect('index')
