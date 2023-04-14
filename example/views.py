from django.shortcuts import redirect, render
from .models import Team_Name, Member, Team_Member
from .forms import ContactUsForm, TeamMembersUpdateForm
from .forms import MemberInformationUpdateForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def gallery(request):
    return render(request, 'gallery.html')


def team(request):
    head_team = Team_Name.objects.get(name="Head Team")
    technical_team = Team_Name.objects.get(name="Technical Team")
    content_team = Team_Name.objects.get(name="Content Team")
    social_team = Team_Name.objects.get(name="Social Team")
    event_team = Team_Name.objects.get(name="Event Team")
    web_team = Team_Name.objects.get(name="Web-D Team")
    head_team_members = Member.objects.filter(team_name=head_team)
    technical_team_lead = Member.objects.filter(team_name=technical_team).first()
    content_team_lead = Member.objects.filter(team_name=content_team).first()
    social_team_lead = Member.objects.filter(team_name=social_team).first()
    event_team_lead = Member.objects.filter(team_name=event_team).first()
    web_team_lead = Member.objects.filter(team_name=web_team).first()
    return render(request, 'team.html', {
        'head_team': head_team_members,
        'tech_lead': technical_team_lead,
        'content_lead': content_team_lead,
        'social_lead': social_team_lead,
        'event_lead': event_team_lead,
        'web_lead': web_team_lead
    })


def blog(request):
    return render(request, 'blog.html')


def magazine(request):
    return render(request, 'magazine.html')


def contact(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'contact.html', {
        'form': form
    })


def team_page(request, slug):
    team = Team_Member.objects.filter(slug=slug).first()
    return render(request, 'team_page.html', {
        'team': team
    })


@login_required
def edit_details(request):
    members = Member.objects.all()
    technical_team = Team_Name.objects.get(name="Technical Team")
    content_team = Team_Name.objects.get(name="Content Team")
    social_team = Team_Name.objects.get(name="Social Team")
    event_team = Team_Name.objects.get(name="Event Team")
    web_team = Team_Name.objects.get(name="Web-D Team")
    head_members = Team_Member.objects.all().first()
    technical_members = Team_Member.objects.filter(team_name=technical_team).first()
    content_members = Team_Member.objects.filter(team_name=content_team).first()
    social_members = Team_Member.objects.filter(team_name=social_team).first()
    event_members = Team_Member.objects.filter(team_name=event_team).first()
    web_members = Team_Member.objects.filter(team_name=web_team).first()
    return render(request, 'edit_details.html', {
        'members': members,
        'head_members': head_members,
        'technical_members': technical_members,
        'content_members': content_members,
        'social_members': social_members,
        'event_members': event_members,
        'web_members': web_members
    })

 
def team_members_update(request, slug):
    team = Team_Member.objects.get(slug=slug)
    form = TeamMembersUpdateForm(instance=team)
    if request.method == 'POST':
        form = TeamMembersUpdateForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('edit-details')
    return render(request, 'team_update.html', {
        'form': form
    })


def add_member(request):
    form = MemberInformationUpdateForm()
    if request.method == 'POST':
        form = MemberInformationUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('edit-details')
    return render(request, 'add_member.html', {
        'form': form
    })


def member_information(request, slug):
    member = Member.objects.get(slug=slug)
    form = MemberInformationUpdateForm(instance=member)
    if request.method == 'POST':
        form = MemberInformationUpdateForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('edit-details')
    return render(request, 'update_member.html', {
        'form': form,
        'member': member
    })


def delete_member(request, slug):
    member = Member.objects.get(slug=slug)
    if request.method == 'POST':
        member.delete()
        return redirect('edit-details')
