# Helper functions only, no import of models at top-level

def get_user_profile(user_id):
    from .models import UserProfile
    return UserProfile.objects.get(user_id=user_id)







