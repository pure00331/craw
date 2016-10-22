from django.contrib import admin
from models import Ariticle

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', "update_time")

admin.site.register(Ariticle, ArticleAdmin)