from django.shortcuts import render
from .models import Newsletter
from django.core.paginator import Paginator


def welcome(request):
    paginator = Paginator(Newsletter.objects.all().order_by('-created_at'), 10)

    return render(request, 'main/welcome.html')
