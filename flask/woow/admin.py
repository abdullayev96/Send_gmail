from django.contrib import admin
from .models import Customer, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ( 'id','title', 'body', 'image', 'create')
    list_display_links = ('id', 'title')
    search_fields = ('title')

admin.site.register(Customer)
admin.site.register(Post)
