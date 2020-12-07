from django.db import models
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey


class Page(models.Model):

    title = models.CharField(max_length=300)
    contents = models.ManyToManyField("BaseContent", related_name='pages', through='PageContents')

    def __str__(self):
        return self.title


class PageContents(SortableMixin):
    page = models.ForeignKey('Page', on_delete=models.CASCADE)
    content = SortableForeignKey("BaseContent", on_delete=models.CASCADE, related_name='pgs')
    content_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ('content_order',)


class BaseContent(models.Model):
    title = models.CharField(max_length=300, default='')
    counter = models.PositiveIntegerField(default=0)

    class Meta:
        pass

    def __str__(self):
        return self.title


class ContentVideo(BaseContent):

    video_url = models.URLField()
    subtitle_url = models.URLField()


class ContentAudio(BaseContent):

    bitrate = models.PositiveIntegerField(default=0)


class ContentText(BaseContent):

    text = models.TextField()

