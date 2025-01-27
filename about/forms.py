# about/forms.py
from django import forms
from .models import ContactMessage, NewsletterSubscriber

class ContactMessageForm(forms.ModelForm):
    # Explicitly define fields to control order and widgets
    name = forms.CharField(
        label="Your Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
    )
    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'placeholder': 'Type your message here...', 'rows': 4}),
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']  # Ensure this includes all fields

class NewsletterSignupForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email for Newsletter",
        widget=forms.EmailInput(attrs={'placeholder': 'Subscribe with your email'}),
    )

    class Meta:
        model = NewsletterSubscriber
        fields = ['name', 'email' ]