from django.db import models

from oneup.main.views import article


# Create your models here.
# Okay bro 😎

class Articles(models.Model):
    title = models.CharField('Назва', max_length= 50)
    articletext = models.TextField('Текст Статті')
    def __str__(self):
        return self.title

class Comments(models.Model):
    name = models.CharField('Ім`я', max_length= 20)
    email = models.EmailField('example@gmail.com')
    commenttext = models.TextField('Текст коментаря', max_length= 200)
    articlekey = models.ForeignKey(Articles, on_delete= models.CASCADE)

    def __str__(self):
        return self.name