from django.test import TestCase
from core.models import Poll


class PollModelTest(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(
            question='teste',
            option_one='django',
            option_two='flask',
            option_three='bottle',
            option_one_count=3,
            option_two_count=3,
            option_three_count=3,
        )
    def test_str_object(self):
        expected = 'teste'
        self.assertEqual(self.poll.__str__(), expected)

    def test_func_total(self):
        self.assertEqual(self.poll.total(), 9)
