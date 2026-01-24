import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import SoulProfile

# 1. Delete file from disk when Profile is deleted
@receiver(post_delete, sender=SoulProfile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.resurrection_scroll:
        if os.path.isfile(instance.resurrection_scroll.path):
            os.remove(instance.resurrection_scroll.path)

# 2. Delete OLD file from disk when NEW file is uploaded
@receiver(pre_save, sender=SoulProfile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = SoulProfile.objects.get(pk=instance.pk).resurrection_scroll
    except SoulProfile.DoesNotExist:
        return False

    new_file = instance.resurrection_scroll
    
    # If there was an old file, and it's different from the new one
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)