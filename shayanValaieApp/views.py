from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail


# Create your views here.


def home(request):
    return render(request, "home.html")


def press(request):
    return render(request, "press.html")


def thankyou(request):
    return render(request, "thankyou.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
        }

        message = '''
        New message: {}

        From: {}

        '''.format(data['message'], data['email'])
        send_mail(data["subject"], message, '', ['svalaiemusic@gmail.com'])
    return render(request, "contact.html", {})
