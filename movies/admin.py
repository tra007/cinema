from django.contrib import admin
from .models import MovieCategory, Movie


# Register your models here.

@admin.register(MovieCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    search_fields = ["name", "slug", ]
    list_filter = ["category", "status"]
    prepopulated_fields = {'slug': ('name',)}
