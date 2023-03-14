from django.db import models

# DB 테이블을 하나 만든다고 생각!
class Post(models.Model):
    # 제목은 최대 길이 30으로 설정
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField()

    def __str__(self):
        return f'[{self.pk}] {self.title}'


