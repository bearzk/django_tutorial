import datetime
import json

from django.db import models
from django.utils import timezone
from annoying.fields import JSONField

class Author(models.Model):
    nickname = models.CharField(max_length=64, unique=True)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nickname

    def __str__(self):
        return unicode(self).encode('utf8')


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    pub_date = models.DateTimeField('date published')
    content = models.TextField(max_length=20000)
    keywords = JSONField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return unicode(self).encode('utf8')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published_recently?'
