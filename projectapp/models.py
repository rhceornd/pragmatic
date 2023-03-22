from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)

    # Project_object(1) 라는 이름을 번호와 제목으로 표현 (article/create에서 확인)
    def __str__(self):
        return f'{self.pk} : {self.title}'