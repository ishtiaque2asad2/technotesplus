import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_share_notification_email(sender,to):
    message = Mail(
        from_email=sender,
        to_emails=to,
        subject='A Note has been shared with you',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('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'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))


def send_reminder_notification_email(sender,to):
    message = Mail(
        from_email=sender,
        to_emails=to,
        subject='Reminder that you have not viewed your note yet',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('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'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))