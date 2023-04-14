from django import forms
from .models import ContactUs


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
