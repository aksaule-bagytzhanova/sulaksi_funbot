from django.contrib import admin
from . import models
# Register your models here.


class WordAdmin(admin.ModelAdmin):
    list_display = ['pk', 'part_of_word', 'word']
    list_editable = ['part_of_word', 'word']


admin.site.register(models.Words, WordAdmin)

