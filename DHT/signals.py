# accounts/signals.py
from django.core.mail import send_mail
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf import settings
from twilio.rest import Client
import requests

User = get_user_model()



@receiver(post_save, sender=User)
def send_registration_alerts(sender, instance, created, **kwargs):
    if created:
        # Prepare alert message
        alert_message = f'''
        New user registered:
        Username: {instance.username}
        Email: {instance.email}
        Registration time: {instance.date_joined}
        '''

        # 1. Send Email Alert
        subject = 'New User Registration Alert'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['zakariameziane66@gmail.com']  # Your admin email
        send_mail(subject, alert_message, email_from, recipient_list)

        # 2. Send WhatsApp Alert (using your existing Twilio setup)
        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            message_whatsapp = client.messages.create(
                from_='whatsapp:+14155238886',
                body=f'🚀 New user registered: {instance.username}',
                to='whatsapp:+212687656704'
            )
        except Exception as e:
            print(f"WhatsApp alert failed: {str(e)}")

        # 3. Send Telegram Alert
        try:
            telegram_token = settings.TELEGRAM_TOKEN
            chat_id = settings.TELEGRAM_CHAT_ID
            send_telegram_message(telegram_token, chat_id,
                                  f"📝 New registration: {instance.username} ({instance.email})")
        except Exception as e:
            print(f"Telegram alert failed: {str(e)}")

        # 4. Send Welcome Email to User
        user_subject = 'Welcome to Temperature Monitoring System'
        user_message = f'''
        Hi {instance.username},

        Your account has been successfully created!

        You can now log in to monitor your temperature sensors.

        Best regards,
        Temperature Monitoring Team
        '''
        send_mail(user_subject, user_message, None, [instance.email])