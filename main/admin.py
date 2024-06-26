from django.contrib import admin
from .models import Newsletter, Announcement, Pages


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'file', 'created_at')
    list_display_links = ('id', 'name', 'image', 'file', 'created_at')
    search_fields = ('id', 'name', 'image', 'file', 'created_at')
    filter = ('name', 'image')


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'created_at')
    list_display_links = ('id', 'name', 'image', 'created_at')
    search_fields = ('id', 'name')


class PagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short', 'created_at')
    list_display_links = ('id', 'name', 'short', 'created_at')
    filter = ('id', 'name', 'created_at')


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Pages, PagesAdmin)
