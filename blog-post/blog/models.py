from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from froala_editor.fields import FroalaField
from .helper import *
from django.urls import reverse
# Create your models here.


class Category(models.Model):

    ABOUT=[
        ('Hacking','Hacking'),
        ('Tech','Tech'),
        ('Programming','programming'),
        ('Software','Software'),


    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    about=models.CharField(max_length=200,null=False,blank=False,choices=ABOUT)
    def __str__(self):
        return self.about


class BlogModel(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    image = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    
  
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(BlogModel, self).save(*args, **kwargs)
        
    def get_absolute_url(self): # new
      return reverse('post_detail', args=[self.slug])
    
