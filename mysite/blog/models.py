from django.db import models
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils import timezone 
import datetime



# Create your models here.



#categories
class Category(models.Model):
    title= models.CharField(max_length=255)
    description= models.CharField(max_length=300)
    def __str__(self):
        return self.title
    
#Articles
class Article(models.Model):
 
   # categories=models.ManyToManyField(Category,blank=True)
    title= models.CharField(max_length=300)
    description= models.TextField()
    cover = models.ImageField(upload_to='images/')
 
    def __str__(self):
        return self.title
    

#post
class Post(models.Model): 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=200) 
    text = models.TextField() 
    created_date = models.DateTimeField(default=datetime.date.today) 
    published_date = models.DateTimeField(blank=True, null=True) 
    categories=models.ManyToManyField(Category,blank=True)

    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 

    def __str__(self): 
        return self.title 

    