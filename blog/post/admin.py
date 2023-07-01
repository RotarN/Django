from django.contrib import admin

# Register your models here.


from .models import Post


#

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'created_date', 'id']


admin.site.register(Post, PostAdmin)
