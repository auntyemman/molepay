from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import User
from .models import User
# from django.conf import settings

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    print(f"------.")
    if created:
        print(f"User signal for {instance.email} created.")
        from .tasks import send_welcome_email
        send_welcome_email.delay(instance.id)
