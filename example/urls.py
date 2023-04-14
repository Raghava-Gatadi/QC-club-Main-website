from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('magazines/', views.magazine, name='magazine'),
    path('contact/', views.contact, name='contact'),
    path('team/<slug:slug>', views.team_page, name='team-page'),
    path('update/<slug:slug>', views.team_members_update, name='update-team'),
    path('add-member/', views.add_member, name='add-member'),
    path('update-member/<slug:slug>',
         views.member_information, name='update-member'),
    path('delete-member/<slug:slug>', views.delete_member, name='delete-member'),
    path('edit-details', views.edit_details, name='edit-details')
]
