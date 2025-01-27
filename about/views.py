from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import About, ContactMessage, NewsletterSubscriber, UserProfile # Import models
from .forms import ContactMessageForm, NewsletterSignupForm, ProfileForm

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

def about(request):
    User_profile = None
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
            
        else:
            form = ProfileForm(instance=user_profile)
    
    return render(request, "about/about.html", {
        "user_profile": user_profile,
        "form": form if request.user.is_authenticated else None,
    })

def about(request):
    about_content = About.objects.first()

    user_profile = None
    form = None

    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = UserProfile(user=request.user)

        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
        else:
            form = ProfileForm(instance=user_profile)
        
    return render(request, "about/about.html", {
        "about": about_content,
        "user_profile": user_profile,
        "form": form,
    })