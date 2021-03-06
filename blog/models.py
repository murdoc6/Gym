from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Name",unique=True)
    created = models.DateTimeField(verbose_name= "Creation Date", auto_now_add=True)
    updated = models.DateTimeField(verbose_name= "Updation Date", auto_now_add=True)


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    published = models.BooleanField(default=True)
    image = models.ImageField(verbose_name="Image",upload_to="blog", null=True,blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                 processors=[ResizeToFill(345, 345)],
                                 format='JPEG',
                                 options={'quality': 60})
    author = models.ForeignKey(User,verbose_name="Author",on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name="get_posts")
    created = models.DateTimeField(verbose_name= "Creation Date", auto_now_add=True)
    updated = models.DateTimeField(verbose_name= "Updation Date", auto_now_add=True)


    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created']

    def __str__(self):
        return self.title
        