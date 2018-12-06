from django.db import models

from django.conf import settings
from django.urls import reverse
from django.db import models
# from exitdjango.db.models.signals import post_save
# from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

DIR_PHOTOS_BLOG = 'Images/PhotosBlog/'
# from .signals import save_comment

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("titre"))
    slug = models.SlugField("Reference",unique=True)
    bodytext = models.TextField(verbose_name=_("message"))
    image = models.ImageField("Photo", upload_to=DIR_PHOTOS_BLOG, blank=True, default = "")

    post_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("post date"))
    modified = models.DateTimeField(null=True, verbose_name=_("modified"))
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                  verbose_name=_("posted by"),
                                  on_delete=models.SET_NULL)

    allow_comments = models.BooleanField(
        default=True, verbose_name=_("allow comments"))
    comment_count = models.IntegerField(
        blank=True, default=0, verbose_name=_('comment count'))
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-post_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
            'year': '%04d' % self.post_date.year,
            'month': '%02d' % self.post_date.month,
            'day': '%02d' % self.post_date.day,
        }

        return reverse('blog_detail', kwargs=kwargs)

