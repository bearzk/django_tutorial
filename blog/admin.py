from django.contrib import admin
from blog.models import Post, Author

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['title']
    fieldsets = [
        ('Title of the Post', {'fields': ['title']}),
        ('Slug of the Post', {'fields': ['slug']}),
        ('Post text body', {'fields': ['content']}),
    ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'created_on', 'updated_on']
    list_filter = ['nickname']
    search_fields = ['nickname']

admin.site.register(Post, PostAdmin)

admin.site.register(Author, AuthorAdmin)
