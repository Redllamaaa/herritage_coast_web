from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Staff
import os

@receiver(pre_save, sender=Staff)
def delete_old_photo_on_change(sender, instance, **kwargs):
    """
    Deletes old image file from disk when replacing with a new one.
    """
    if not instance.pk:
        return  # new staff, nothing to delete

    try:
        old_file = Staff.objects.get(pk=instance.pk).photo
    except Staff.DoesNotExist:
        return

    new_file = instance.photo
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

@receiver(post_delete, sender=Staff)
def delete_photo_on_delete(sender, instance, **kwargs):
    """
    Deletes image file from disk when staff is deleted.
    """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)
