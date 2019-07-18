from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    author = models.TextField(verbose_name='저자')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    #migrate : DB에 맞는 자료형으로 바꿔준다