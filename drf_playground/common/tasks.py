from django.core.mail import EmailMessage
from config import celery_app


@celery_app.task()
def send_email(mail_subject, message, to, html=False):
    """
    Send email to user.

    :param str mail_subject: The subject of the email
    :param str message: The body of the email
    :param list(str) to: List of email recipients
    :param bool html: Send email as html or plain text
    """
    email = EmailMessage(mail_subject, message, to=to)
    email.content_subtype = "html" if html else "text"
    email.send()
