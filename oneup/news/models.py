from datetime import datetime

from django.conf.urls.static import static
from django.db import models
from django.utils.functional import empty
from django_ckeditor_5.fields import CKEditor5Field
# from oneup.main.views import article


# Create your models here.
# Okay bro 😎

class Articles(models.Model):
    title = models.CharField("Назва", max_length= 50)
    previewimage = models.ImageField("Превью", upload_to="uploads/",height_field=None, width_field=None, max_length=50,default= "news/static/img/placeholder.png")
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

    def getviews(self):
        return self.interactions.count()

    def getlikes(self):
        return self.interactions.filter(is_like=True).count()

    def getdislikes(self):
        return self.interactions.filter(is_like=False).count()

    def getrating(self):
        return self.getlikes() - self.getdislikes()

    def getcommentsamount(self):
        return self.comments.count()

    def addlike(self, userip): # лайк
        self.view(userip)
        reaction = self.interactions.filter(user=userip).first()
        lik = reaction.is_like
        if lik is None:
            reaction.is_like = True
        elif lik is True:
            reaction.is_like = None
        elif lik is False:
            reaction.is_like = True
        reaction.save()

    def adddislike(self, user_ip): # дизлайк
        self.view(user_ip)
        reaction = self.interactions.filter(user=user_ip).first()
        lik = reaction.is_like
        if lik is None:
            reaction.is_like = False
        elif lik is True:
            reaction.is_like = False
        elif lik is False:
            reaction.is_like = None
        reaction.save()

    def view(self, user_ip): # перегляд
        reaction = self.interactions.filter(user=user_ip).first()
        if not  reaction:
            reaction = self.interactions.create(user=user_ip, is_like=None)
            reaction.save()


class ArticleReaction(models.Model): # лайк, дизлайк та перегляд
    user = models.GenericIPAddressField('IP - адреса')
    articlekey = models.ForeignKey(Articles,related_name= 'interactions',on_delete=models.CASCADE)
    is_like = models.BooleanField('Лайк', null=True, blank=True)  # True — лайк, False — дизлайк, None — перегляд

    def __str__(self):
        return f'{self.user} -> {self.articlekey}'

    class Meta:
        verbose_name = 'Взаємодія'
        verbose_name_plural = 'Взаємодії'
class Comments(models.Model):
    name = models.CharField('Ім`я', max_length= 20)
    email = models.EmailField('example@gmail.com')
    commenttext = models.TextField('Текст коментаря', max_length= 200)
    articlekey = models.ForeignKey(Articles,related_name="comments",on_delete= models.CASCADE)
    date = models.DateField('Дата публікації', auto_now_add= True)
    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
    def __str__(self):
        return f'{self.name} -> {self.articlekey.title}'