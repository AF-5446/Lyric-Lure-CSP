from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import About, ContactMessage, NewsletterSubscriber, UserProfile # Import models
from .forms import ContactMessageForm, NewsletterSignupForm

def about(request):
    """Render the About page with separate forms."""
    about_instance = About.objects.first()  # Simplified query

    # Initialize empty forms (for GET requests)
    contact_form = ContactMessageForm()
    newsletter_form = NewsletterSignupForm()

    # Handle Contact Form Submission
    if 'contact_submit' in request.POST:
        contact_form = ContactMessageForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Message sent! We'll respond soon.")
            return redirect('about')  # Redirect to clear POST data

    # Handle Newsletter Form Submission
    elif 'newsletter_submit' in request.POST:
        newsletter_form = NewsletterSignupForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, "Thanks for signing up!")
            return redirect('about')

    return render(request, "about/about.html", {
        "about": about_instance,
        "contact_form": contact_form,
        "newsletter_form": newsletter_form,
    })

def about(request):
    # For logged-in users: Fetch their profile
    user_profile = None
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    return render(request, "about/about.html", {
        "user_profile": user_profile,
    })