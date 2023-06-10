import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from authors_api.settings.base import AUTH_USER_MODEL
from core_apps.profiles.models import Profile

logger = logging.getLogger(__name__)


# So in our post Save signal here at the receiver, the sender represents the modal class that triggers
# the signal.
# In this case, the sender is the user modal.
# Then here, within our create user profile method, the instance parameter represents the specific instance
# of the modal that triggered the signal.
# Then created parameter represents a boolean value that indicates whether the instance was created or
# updated.
@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"{instance}'s profile has been created.")
