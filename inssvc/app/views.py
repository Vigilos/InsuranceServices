import smtplib
from pathlib import Path
from email.message import EmailMessage
from string import Template
import os
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from dotenv import load_dotenv
from .forms import EmailForm

load_dotenv()


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def product1(request):
    return render(request, "product1.html")


def product2(request):
    return render(request, "product2.html")


def product3(request):
    return render(request, "product3.html")


def contact_us(request):
    if request.method == "POST" or None:
        form = EmailForm(request.POST or None)
        if form.is_valid():
            send_email_response = send_email(request.POST)
            if send_email_response == 'Email Sent':
                messages.success(
                    request, 'Thank you! Your request was submitted successfully.')
            else:
                error_message = 'An error occurred and the message was not sent. ' + send_email_response
                messages.error(request, error_message)
            return HttpResponseRedirect('/contact-us')
        else:
            messages.error(
                request, 'Your message wasn\'t sent yet. Please, see entry errors below.')
            return render(request, 'contact-us.html', {'form': form})
    else:
        form = EmailForm()
        return render(request, 'contact-us.html', {'form': form})


def send_email(request):

    try:
        file_path = Path(__file__).parent.resolve()
        html = Template(
            Path(f'{file_path}/email_content.html').read_text())
        email = EmailMessage()
        email['from'] = "test@knightskeep.com"
        email['to'] = "joe@inssvc.com"
        email['subject'] = "From Contact Us Form"

        email_data = dict(request)
        email_data.pop('csrfmiddlewaretoken')

        for key, item in email_data.items():
            if key == 'name':
                name = ''.join(item)
            if key == 'email_address':
                email_address = ''.join(item)
            if key == 'phone':
                phone = ''.join(item)
            if key == 'message':
                message = ''.join(item)

        email_data.pop('name')
        email_data.pop('email_address')
        email_data.pop('phone')
        email_data.pop('message')

        key_list = []
        for key in email_data.keys():
            key_list.append(key)
        insurance = ', '.join(key_list)

        date_time = timezone.localtime().strftime("%m/%d/%Y %H:%M:%S (PT)")
        email.set_content(html.substitute(name=name, email_address=email_address,
                          phone=phone, insurance=insurance, message=message, sent=date_time), 'html')
        with smtplib.SMTP_SSL(host='mail.knightskeep.com', port=465, timeout=30) as smtp:
            smtp.ehlo()
            smtp.login(os.getenv('USER_NAME'), os.getenv('PASS'))
            smtp.send_message(email)

        return 'Email Sent'

    except Exception as err:
        return str(err)
