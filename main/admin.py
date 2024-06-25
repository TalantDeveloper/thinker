from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'file', 'created_at')
    list_display_links = ('id', 'name', 'image', 'file', 'created_at')
    search_fields = ('id', 'name', 'image', 'file', 'created_at')


admin.site.register(Newsletter, NewsletterAdmin)

