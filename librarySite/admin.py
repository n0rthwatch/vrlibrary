from django.contrib import admin

from librarySite.models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'pages_count', 'downloads_count', 'author']


class BookInLine(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [BookInLine]


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']


admin.site.register(News, NewsAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
