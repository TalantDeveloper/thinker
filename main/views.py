from django.shortcuts import render
from .models import Newsletter, Announcement, Pages, Welcome
from django.core.paginator import Paginator


def welcome(request):
    newsletters = Newsletter.objects.all().order_by('-created_at')[:5]
    announcements = Announcement.objects.all()[:4]
    welcom = Welcome.objects.all().first()
    context = {
        'newsletters': newsletters,
        'announcements': announcements,
        'welcom': welcom
    }
    return render(request, 'main/welcome.html', context)


def newsletters_view(request):
    p = Paginator(Newsletter.objects.all().order_by('-created_at'), 10)
    page = request.GET.get('page')
    newsletters = p.get_page(page)
    return render(request, 'main/newsletters.html', {'newsletters': newsletters})


def newsletter_view(request, newsletter_id):
    newsletter = Newsletter.objects.get(pk=newsletter_id)
    newsletter.sees += 1
    newsletter.save()
    context = {'newsletter': newsletter}
    return render(request, 'main/detail.html', context)


def announcements_view(request):
    p = Paginator(Announcement.objects.all().order_by('-created_at'), 3)
    page = request.GET.get('page')
    announcements = p.get_page(page)
    context = {'announcements': announcements}
    return render(request, 'main/announs.html', context)


def announcement_view(request, announcement_id):
    announcement = Announcement.objects.get(pk=announcement_id)
    context = {'announcement': announcement}
    return render(request, 'main/announ.html', context)


def page_view(request, page):
    page = Pages.objects.get(short=page)

    return render(request, 'main/page.html', {'page': page})