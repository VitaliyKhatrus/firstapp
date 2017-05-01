# -*- coding: utf-8 -*-
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
# from django.contrib.auth.models import User


# Create your models here.

SHORT_TEXT_LEN = 250


class Article(models.Model):
    class Meta():
        ordering = ('-article_date',)  # sorting by date
        db_table = "article"  # table`s name

    article_title = models.CharField(max_length = 200)
    # article_text = models.TextField()
    article_text = RichTextUploadingField(blank=True, default='')
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default = 0)
    article_dislikes = models.IntegerField(default = 0)

    def __unicode__ (self):    # output article title in admin panel
        return self.article_title

    def get_short_text(self):      # short text our articles - articles.html
        if len(self.article_text) > SHORT_TEXT_LEN:
            return self.article_text[:SHORT_TEXT_LEN]
        else:
            return self.article_text


class Comments(models.Model):
    class Meta():
        db_table = "comments"#table`s name
    
    comments_text = models.TextField(verbose_name='Текст комментария:')
    comments_article = models.ForeignKey(Article)
    #comments_username = models.ManyToManyField(User)
    comments_username = models.CharField(max_length = 100, default = None)




