from django.db import models

# Create your models here.
class Comic(models.Model):
    title = models.CharField(max_length=256)
    publish_date = models.DateTimeField(help_text='The date and time this comic shall appear online.')
    imgurl = models.CharField(max_length=1024)
    def newer_id(self):
        try:
            return Comic.objects.filter(id__gt=self.id).order_by('id')[0].id
        except IndexError:
            return None
    def older_id(self):
        try:
            return Comic.objects.filter(id__lt=self.id).order_by('-id')[0].id
        except IndexError:
            return None
