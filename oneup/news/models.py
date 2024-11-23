from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# from oneup.main.views import article


# Create your models here.
# Okay bro 😎

class Articles(models.Model):
    title = models.CharField("Назва", max_length= 50)
    articletext = CKEditor5Field('Текст Статті')
    date = models.DateField('Дата публікації', auto_now_add = True)

    class ChooseType(models.TextChoices): # вибір типу новини
        NEWS = 'огляд', 'огляд' # я хз нафіга два рази якщо чесно але так треба
        SELECTIONS = 'підбірка', 'підбірка'
        ARTICLE = 'стаття', 'стаття'
    articletype = models.CharField('Тип новини',choices = ChooseType.choices,default = ChooseType.ARTICLE, max_length= 20)

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

    def __str__(self):
        return self.title

class ArticleReaction: # лайк, дизлайк та перегляд
    user = models.GenericIPAddressField('IP - адреса')
    articlekey = models.ForeignKey(Articles, related_name="reactions", on_delete=models.CASCADE)
    is_like = models.BooleanField('Лайк', null=True, blank=True)  # True — лайк, False — дизлайк, None — перегляд

class Comments(models.Model):
    name = models.CharField('Ім`я', max_length= 20)
    email = models.EmailField('example@gmail.com')
    commenttext = models.TextField('Текст коментаря', max_length= 200)
    articlekey = models.ForeignKey(Articles, related_name= "comments" ,on_delete= models.CASCADE)
    date = models.DateField('Дата публікації', auto_now_add= True)
    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
    def __str__(self):
        return self.name