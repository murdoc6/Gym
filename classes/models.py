from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Class(models.Model):
    title = models.CharField(max_length=100, verbose_name = "Title" )
    subtitle = RichTextField(verbose_name = "Subtitle" )
    content = RichTextField(verbose_name = "Content" )
    image = models.ImageField(verbose_name= "Image", upload_to= "classes" )
    image_thumbnail = ImageSpecField(source='image',
                                 processors=[ResizeToFill(345, 345)],
                                 format='JPEG',
                                 options={'quality': 60})
    created = models.DateTimeField(verbose_name= "Creation Date", auto_now_add=True)
    updated = models.DateTimeField(verbose_name= "Updation Date", auto_now_add=True)


    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ['-created']

    def __str__(self):
        return self.title
        
