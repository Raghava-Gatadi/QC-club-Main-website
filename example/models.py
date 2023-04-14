from django.db import models
from django.utils.text import slugify


class Team_Name(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default="")

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    team_name = models.ForeignKey("Team_Name", on_delete=models.CASCADE)
    position = models.CharField(max_length=50, blank=True, null=True)
    profile_photo = models.ImageField(
        upload_to="profile_photos", default="default_profile.png")
    linked_in = models.TextField(default='', blank=True)
    github = models.TextField(default='', blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ['position', 'name']

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.position}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}, {self.team_name}, {self.position}"


class Team_Member(models.Model):
    team = models.ForeignKey(
        "Team_Name", on_delete=models.CASCADE, blank=False, default='')
    team_name = models.CharField(
        max_length=50, blank=False, null=False, default='')
    members = models.ManyToManyField("Member", blank=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.team_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.team_name}"


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.subject}"
