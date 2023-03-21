from django.db import models

# DB 테이블을 하나 만든다고 생각!
class Post(models.Model):
    # 제목은 최대 길이 30으로 설정
    title = models.CharField(max_length=30)
    # content를 빼먹고 글을 작성했는데 다시 작성하고 하니까 오류남...
    content = models.TextField(default='')

    created_at = models.DateTimeField()

    def __str__(self):
        return f'[{self.pk}] {self.title}'


