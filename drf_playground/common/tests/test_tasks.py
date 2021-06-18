from django.test import TestCase
from drf_playground.common.tasks import send_email
from mock import patch
from pytest import mark


@mark.common
@mark.common_tasks
class TestTasks(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestTasks, cls).setUpClass()

    @patch("drf_playground.common.tasks.EmailMessage")
    def test_send_email(self, email):
        mail_subject = "Subject"
        message = "This is a message"
        to = ["test@test.com"]
        send_email(mail_subject, message, to)
        email().send.assert_called_once()
