from django.test import TestCase
from django.shortcuts import resolve_url as r
from core.models import Poll


class CoreTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r("home"))
        self.poll = Poll.objects.create(
            question="teste", option_one=3, option_two=3, option_three=3,
        )

    def test_get_status_code_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, "poll/index.html")

    def test_exists_url_create_poll(self):
        expected = 'href="{}"'.format(r("create"))

        self.assertContains(self.response, expected)

    def test_polls(self):
        expected = "Available Polls"

        self.assertContains(self.response, expected)

    def test_view_create_post(self):
        response = self.client.post(
            r("create"),
            {
                "question": "teste",
                "option_one": "teste1",
                "option_two": "teste2",
                "option_three": "test3",
            },
        )

        self.assertEqual(response.status_code, 302)

    def test_view_create_status_code_200(self):
        response = self.client.get(r("create"))

        self.assertEqual(200, response.status_code)

    def test_view_vote(self):
        response1 = self.client.post(
            r("vote", pk=self.poll.id), data={"poll": "option1"}
        )
        response2 = self.client.post(
            r("vote", pk=self.poll.id), data={"poll": "option2"}
        )
        response3 = self.client.post(
            r("vote", pk=self.poll.id), data={"poll": "option3"}
        )

        self.assertEqual(302, response1.status_code)
        self.assertEqual(302, response2.status_code)
        self.assertEqual(302, response3.status_code)

    def test_view_vote_error_400(self):
        response = self.client.post(
            r("vote", pk=self.poll.id), data={'poll': 'sdfsf'})

        self.assertEqual(200, response.status_code)

    def test_view_vote_status_code_200(self):
        response = self.client.get(r("vote", pk=(self.poll.id)))

        self.assertEqual(200, response.status_code)

    def test_view_result_status_code_200(self):
        response = self.client.get(r("result", pk=(self.poll.id)))

        self.assertEqual(200, response.status_code)
