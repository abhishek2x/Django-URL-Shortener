from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from shortener.models import Person


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwarg):
    if created:
        Person.objects.create(user=instance, name=instance.username)

