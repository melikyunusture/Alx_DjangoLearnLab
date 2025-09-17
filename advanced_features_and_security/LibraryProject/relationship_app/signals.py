from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import UserProfile
from relationship_app.models import RelationshipUserProfile


@receiver(post_save, sender=UserProfile)
def create_relationship_profile(sender, instance, created, **kwargs):
    if created:
        RelationshipUserProfile.objects.create(user_profile=instance)


@receiver(post_save, sender=UserProfile)
def save_relationship_profile(sender, instance, **kwargs):
    try:
        instance.relationship_profile.save()
    except RelationshipUserProfile.DoesNotExist:
        RelationshipUserProfile.objects.create(user_profile=instance)