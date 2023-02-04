import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path, PurePath
import csv
from flask import Flask, render_template, request, redirect
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/<string:page_name>")
def go_to_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    try:
        email, subject, message = data.values()
        with open('./database.csv', mode='a', encoding='utf-8') as db_file:
            csv_writer = csv.writer(
                db_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, message])
    except Exception as err:
        print('Oops, something went wrong with saving to database file')
        print(err)
        exit()


def send_email(data):
    try:
        file_path = Path(__file__).parent.resolve()
        html = Template(Path(f'{file_path}/email_content.html').read_text())
        email = EmailMessage()
        email['from'] = "test@knightskeep.com"
        email['to'] = "admin@knightskeep.com"
        email['subject'] = "From Contact Us Form"

        date_time = datetime.now(timezone.utc)
        date_time = date_time.astimezone(
            ZoneInfo('US/Pacific')).strftime("%m/%d/%Y %H:%M:%S (PT)")
        email_address, subject, message = data.values()
        email.set_content(html.substitute(email=email_address,
                                          subject=subject, message=message, sent=date_time), 'html')

        with smtplib.SMTP(host='encore.websitewelcome.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(os.getenv('USER_NAME'), os.getenv('PASS'))
            smtp.send_message(email)
            return 'Email sent!'

    except Exception as err:
        return ('Something went wrong with send_mail. Error: ' + str(err))


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_csv(data)
            print(send_email(data))
            return redirect('/thankyou.html')
        except Exception as err:
            return ('Something went wrong handling the submit_form POST. Error: ' + str(err))
    else:
        return 'Not a POST request!'
