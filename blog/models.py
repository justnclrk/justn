from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_summernote.fields import SummernoteTextField
from taggit.managers import TaggableManager
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='posts_images')
    content = SummernoteTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)
