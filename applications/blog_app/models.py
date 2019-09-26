from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class blog_post(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_img = models.ImageField(upload_to='images/')
    blog_description = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blog_title}"
