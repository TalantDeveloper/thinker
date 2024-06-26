from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('jurnal/', views.newsletters_view, name='newsletters'),
    path('jurnal/<int:newsletter_id>/', views.newsletter_view, name='newsletter'),

    path('elon/', views.announcements_view, name='announcements'),
    path('elon/<int:announcement_id>/', views.announcement_view, name='announcement'),

    path('page/<str:page>/', views.page_view, name='page'),
]
