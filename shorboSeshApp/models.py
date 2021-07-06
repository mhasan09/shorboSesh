from django.db import models

# Create your models here.

class NEWS(models.Model):

    NEWS_TITLE = models.CharField("NEWS_TITLE", max_length=150, null=True, blank=True)
    NEWS_SUBTITLE = models.TextField("NEWS_SUBTITLE", null=True, blank=True)
    NEWS_LINK = models.TextField("NEWS_LINK", null=True, blank=True)
    NEWS_SOURCE = models.CharField("NEWS_SOURCE", max_length=150, null=True, blank=True)
    POST_CREATED_AT = models.DateTimeField("TIME_STAMP", null=True, blank=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return str(self.NEWS_TITLE) or 'u'