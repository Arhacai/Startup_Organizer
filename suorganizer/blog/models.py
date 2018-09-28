from django.db import models
from organizer.models import Startup, Tag


class Post(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField(
        max_length=35,
        help_text='A label for URL config',
        unique_for_month='pub_date'
    )
    text = models.TextField()
    pub_date = models.DateField('date publised', auto_now_add=True)

    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, 'blog_posts')

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

    def __str__(self):
        return "{} on {}".format(
            self.title, self.pub_date.strftime('%Y-%m-%d')
        )