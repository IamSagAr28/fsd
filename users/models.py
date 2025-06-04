from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    Profile model for the demo version of SkillForge.
    Extends the built-in User model with additional fields.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

# Temporarily commented out to debug server startup issues
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     """Create a Profile for each new User."""
#     if created:
#         Profile.objects.create(user=instance)
# 
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     """Save the Profile when the User is saved."""
#     try:
#         if hasattr(instance, 'profile'):
#             instance.profile.save()
#     except Exception as e:
#         print(f"Error saving profile: {e}")
#         # Silently pass if profile doesn't exist yet
