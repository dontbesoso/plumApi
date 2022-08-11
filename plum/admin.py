from django.contrib import admin
from . import models 
class PracownicyItemAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name', 'cardId', 'description', 'hasAdmin')
    
admin.site.register(models.Pracownicy, PracownicyItemAdmin)

# Register your models here.
"""
from django.contrib import admin 
    admin.site.register(models.FeedItem, FeedItemAdmin)

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    cardId = models.IntegerField()
    description = models.CharField(max_length=255)
    hasAdmin = models.BooleanField()
"""