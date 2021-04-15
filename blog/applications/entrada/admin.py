from django.contrib import admin

from .models import Category, Tag, Entry
# Register your models here.


admin.site.register(Entry)
admin.site.register(Tag)
admin.site.register(Category)


