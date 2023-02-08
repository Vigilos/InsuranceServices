import smtplib
from pathlib import Path
from email.message import EmailMessage
from string import Template
import os
from django.utils import timezone
from django.shortcuts import render
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


def send_email(request):
    if request.POST:
        form = EmailForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print('POST successful!')

        try:
            file_path = Path(__file__).parent.resolve()
            html = Template(
                Path(f'{file_path}/email_content.html').read_text())
            email = EmailMessage()
            email['from'] = "test@knightskeep.com"
            email['to'] = "admin@knightskeep.com"
            email['subject'] = "From Contact Us Form"

            date_time = timezone.localtime().strftime("%m/%d/%Y %H:%M:%S (PT)")
            token, name, email_address, message = request.POST.values()
            email.set_content(html.substitute(name=name, email=email_address,
                                              message=message, sent=date_time), 'html')

            with smtplib.SMTP(host='encore.websitewelcome.com', port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(os.getenv('USER_NAME'), os.getenv('PASS'))
                smtp.send_message(email)

        except Exception as err:
            print('Something went wrong with send_mail. Error: ' + str(err))

    return 'Email sent successfully!'
    # return render(request, 'index.html', {'form': EmailForm})
