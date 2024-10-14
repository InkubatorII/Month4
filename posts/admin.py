from django.contrib import admin
from posts.models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'created_at', 'updated_at')
    search_fields = ('title', 'content')

admin.site.register(Comment)
admin.site.register(Tag)