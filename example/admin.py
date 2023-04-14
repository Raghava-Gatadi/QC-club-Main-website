from django.contrib import admin
from .models import Member, Team_Member, Team_Name, ContactUs


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_name', 'position')


class TeamMembersAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("team_name",)}


# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(Team_Member, TeamMembersAdmin)
admin.site.register(Team_Name)
admin.site.register(ContactUs)
