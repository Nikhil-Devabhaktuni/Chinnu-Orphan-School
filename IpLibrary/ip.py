#Coustom library for sending mail to admin
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
import requests

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    url = f'http://ip-api.com/json/{ip}'
    response = requests.get(url)
    data = response.json()
    location = f"{data['city']}, {data['regionName']}, {data['country']}"
    return ip, location

def send_login_notification(request, user_type):
    user = request.user
    ip_address, location = get_client_ip(request)
    if user_type == 'teacher':
        subject = f'Login Notification: Teacher {user.username} logged in from {ip_address}'
        message = f'Teacher Name: {user.username}\nIP Address: {ip_address}\nLocation: {location}'
    elif user_type == 'admin':
        subject = f'Login Notification: Admin {user.username} logged in from {ip_address}'
        message = f'Admin Name: {user.username}\nIP Address: {ip_address}\nLocation: {location}'
    else:
        subject = f'Login Notification: Student {user.username} logged in from {ip_address}'
        message = f'Student Name: {user.username}\nIP Address: {ip_address}\nLocation: {location}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_RECEIVING_USER], fail_silently=False)
