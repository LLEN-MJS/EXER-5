from django.contrib import admin
from .models import Book, Author, Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name' ]
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(Book)
admin.site.register(Author)


