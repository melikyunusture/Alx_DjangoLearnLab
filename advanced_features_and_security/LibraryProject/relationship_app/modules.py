def do_something_with_relationship(user_profile):
    from .models import RelationshipUserProfile  # local import
    return RelationshipUserProfile.objects.filter(user_profile=user_profile)