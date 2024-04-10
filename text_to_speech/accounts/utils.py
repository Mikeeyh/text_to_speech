from django.conf import settings
from django.template.loader import render_to_string
from mailjet_rest import Client


def send_welcome_email(email):
    mailjet = Client(auth=(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD), version='v3.1')

    html_content = render_to_string('accounts/welcome-email.html', {'username': email})
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "mikeharalanov@gmail.com",
                    "Name": "Speechify"
                },
                "To": [
                    {
                        "Email": email,
                        "Name": email,
                    }
                ],
                "Subject": "Welcome to Speechify!",
                "Text": "Greetings from Speechify!",
                "HTMLPart": html_content
            }
        ]
    }
    result = mailjet.send.create(data=data)
