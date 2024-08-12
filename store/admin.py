from django.contrib import admin

from .models import Game,product,gold,gold1

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','price','in_stock','created','updated']
    list_filter =['in_stock','is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(gold)
class goldadmin(admin.ModelAdmin):
    list_display = ['name', 'texts']

@admin.register(gold1)
class gold1admin(admin.ModelAdmin):
    list_display = ['name', 'texts']



# Register your models here.
