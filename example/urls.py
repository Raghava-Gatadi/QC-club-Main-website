from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('magazines/', views.magazine, name='magazine'),
    path('contact/', views.contact, name='contact'),
    path('team/technical-team',
         views.team_technical, name='team-page-technical'),
    path('team/content-team', views.team_content, name='team-page-content'),
    path('team/social-team', views.team_social, name='team-page-social'),
    path('team/event-team', views.team_event, name='team-page-event'),
    path('team/web-d-team', views.team_webd, name='team-page-webd')
]
