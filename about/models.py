from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"About me for {self.title}"

# Model for "Send a Message" form
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()  # <-- Critical: Ensure this exists!
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

# Model for Newsletter Signup
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)  # Prevent duplicate signups
    name = models.CharField(max_length=100)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "about_profile"
)
    bio = models.TextField(blank=True)
    avatar = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"{self.user.username} profile"