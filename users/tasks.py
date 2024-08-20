from celery import shared_task
from django.core.mail import send_mail
from .repository import UsersRepository
@shared_task
def send_welcome_email(id):
    user_repo = UsersRepository()
    user = user_repo.get_one(id=id)
    print(f"Sending welcome email.")
    send_mail(
        from_email='no-reply@molepay.com',
        recipient_list=[user.email],
        subject='Welcome to MolePay',
        message=f"Welcome {user.first_name} to MolePay. Your account has been created. You can now log in to your account using your email and password.",
        
        fail_silently=False,
    )
    print(f"Sent welcome email to {user.email}.")
