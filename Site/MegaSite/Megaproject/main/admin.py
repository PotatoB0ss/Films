from django.contrib import admin
from .models import *


@admin.register(Films)
class Filmi(admin.ModelAdmin):
    list_display = ('title', 'content', 'year', 'published')
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    filter_horizontal = ['genre']       #Чтобы норм отображалось ManyToMany поле


@admin.register(Genres)
class Fgenr(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Comment)