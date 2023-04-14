from django.shortcuts import redirect, render
from .forms import ContactUsForm


def home(request):
    return render(request, 'home.html')


def gallery(request):
    return render(request, 'gallery.html')


def team(request):
    return render(request, 'teamPages/team.html')


def team_technical(request):
    return render(request, 'teamPages/team_technical.html')


def team_content(request):
    return render(request, 'teamPages/team_content.html')


def team_social(request):
    return render(request, 'teamPages/team_social.html')


def team_event(request):
    return render(request, 'teamPages/team_event.html')


def team_webd(request):
    return render(request, 'teamPages/team_webd.html')


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
