from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category,Article,Post


# Register your models here.


admin.site.site_header='Farnam site'
 
 
admin.site.register(Article)
admin.site.register(Category)



class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','created_date','published_date',)
    list_filter=('created_date','categories',)


admin.site.register(Post, PostsAdmin)


