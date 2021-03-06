from django.test import TestCase
from drf_playground.users.tasks import get_users_count
from mock import patch
from pytest import mark


@mark.users
@mark.users_tasks
class TestTasks(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super(TestTasks, cls).setUpClass()

    @patch("django.contrib.auth.models.User")
    def test_get_users_count(self, user):
        user.objects.count_return_value = 1
        return_value = get_users_count()
        self.assertEqual(1, return_value)
