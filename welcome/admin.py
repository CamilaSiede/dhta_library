from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    pass

admin.site.register(Books)