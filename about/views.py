from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import About, ContactMessage, NewsletterSubscriber, UserProfile
from .forms import ContactMessageForm, NewsletterSignupForm, ProfileForm

def about(request):
    """Render the About page with all forms and profile data."""
    # Public content
    about_instance = About.objects.first()
    
    # Initialize forms
    contact_form = ContactMessageForm()
    newsletter_form = NewsletterSignupForm()
    profile_form = ProfileForm()
    user_profile = None

    # Handle POST submissions
    if request.method == 'POST':
        # Contact Form
        if 'contact_submit' in request.POST:
            contact_form = ContactMessageForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, "Message sent! We'll respond soon.")
                return redirect('about')

        # Newsletter Form
        elif 'newsletter_submit' in request.POST:
            newsletter_form = NewsletterSignupForm(request.POST)
            if newsletter_form.is_valid():
                newsletter_form.save()
                messages.success(request, "Thanks for signing up!")
                return redirect('about')

        # Profile Form (for logged-in users)
        elif 'profile_submit' in request.POST and request.user.is_authenticated:
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Profile updated!")
                return redirect('about')

    # Handle GET requests
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=user_profile)

    return render(request, "about/about.html", {
        "about": about_instance,
        "contact_form": contact_form,
        "newsletter_form": newsletter_form,
        "user_profile": user_profile,
        "profile_form": profile_form,
    })