from django.shortcuts import render

# 전체 경로 가져오면 오류난다!
from .models import Post


# Create your views here.

# 파라미터는 request 외워!
def index(request):
    # 동적 렌더링

    # posts의 순서를 바꾸려면 리스트의 순서를 바꾸면 되잖아?
    # '-' 는 역순을 의미함
    posts = Post.objects.all().order_by('-pk')
    # 사용자 요청을 받아서 여러가지 일을 한다!
    return render(
        request,
        'blog/index.html',
        {
            # 위의 변수 posts를 posts라고 전달한다.
            'posts' : posts,
        }
    )