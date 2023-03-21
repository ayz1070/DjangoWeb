from django.db import models

# DB 테이블을 하나 만든다고 생각!

# 모델은 저장하고 있는 데이터의 필수적인 필드와 동작을 포함하고 있다.
# 일반적으로, 각각의 모델은 하나의 데이터베이스 테이블에 매핑됨.
# 모델을 정의한 후에는 장고에 이 모델을 이용할 것이라고 얘기해줘야한다.
# settings.py 의 INSATLLED_APPS에 우리가 blog라는 모듈을 만들었으니 'blog'를 추가하면 된다!!!

# 여기서 Post는 데이터베이스의 필드가 된다.
class Post(models.Model):
    # title, content는 모델의 필드. 각 필드는 클래스 속성으로 지정되며 각 속성은 각 데이터베이스의 열에 매핑됨.
    # 제목은 최대 길이 30으로 설정
    title = models.CharField(max_length=30)
    # "title" varchar(30) NOT NULL 이런 식으로 데이터베이스 테이블을 생성하는 거지!!!

    # content를 빼먹고 글을 작성했는데 다시 작성하고 하니까 오류남...
    # default =''를 추가하니 실행됨...
    content = models.TextField(default='')

    # ctrl + 스페이스 : 필요 파라미터 제공

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'


