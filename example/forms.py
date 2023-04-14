from django import forms
from .models import ContactUs, Member, Team_Member


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'outline-none bg-[#2b2b2b] w-full px-2 py-1'})
        self.fields['email'].widget.attrs.update(
            {'class': 'outline-none bg-[#2b2b2b] w-full px-2 py-1'})
        self.fields['subject'].widget.attrs.update(
            {'class': 'outline-none bg-[#2b2b2b] w-full px-2 py-1'})
        self.fields['message'].widget.attrs.update(
            {'class': 'outline-none bg-[#2b2b2b] w-full px-2 py-1 h-24'})


class TeamMembersUpdateForm(forms.ModelForm):
    class Meta:
        model = Team_Member
        fields = ['members', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['members'].widget.attrs.update(
            {'class': 'p-2 bg-[#] outline-none h-40 font-semibold rounded-lg'})


class MemberInformationUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'py-1 px-2 outline-none w-52 rounded-xl font-semibold'})
        self.fields['team_name'].widget.attrs.update(
            {'class': 'py-1 px-4 outline-none w-52 rounded-xl font-semibold'})
        self.fields['position'].widget.attrs.update(
            {'class': 'py-1 px-2 outline-none w-52 rounded-xl font-semibold'})
        self.fields['profile_photo'].widget.attrs.update(
            {'class': 'py-1 px-2 outline-none w-52 rounded-xl font-semibold text-gray-300'})
        self.fields['linked_in'].widget.attrs.update(
            {'class': 'py-1 px-2 outline-none w-52 rounded-xl font-semibold text-gray-500 h-9'})
        self.fields['github'].widget.attrs.update(
            {'class': 'py-1 px-2 outline-none w-52 rounded-xl font-semibold text-gray-500 h-9'})
