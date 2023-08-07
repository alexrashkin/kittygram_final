from django.contrib import admin
from .models import *

class AchivementAdmin(admin.ModelAdmin):
    list_display = ('name',)

# class AchuvementCatInline(admin.ModelAdmin):
#     model = AchievementCat
#     extra = 1

class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'birth_year', 'owner')
    # inlines = [AchuvementCatInline]
    list_filter = ('color', 'birth_year', 'owner')

admin.site.register(Achievement, AchivementAdmin)
admin.site.register(Cat, CatAdmin)