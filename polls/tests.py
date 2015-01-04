import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from polls.models import Question

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,
                                   pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No question yet.", status_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_indext_with_a_past_question(self):
        create_question(question_text='from past', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: from past>']
        )

    def test_indext_with_a_future_question(self):
        create_question(question_text='from future', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No question yet.", status_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_indext_with_future_question_and_past_question(self):
        create_question(question_text='from future', days=30)
        create_question(question_text='from past', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],
                                 ["<Question: from past>"])

    def test_index_views_with_two_past_questions(self):
        create_question(question_text='1st old', days=-30)
        create_question(question_text='2nd old', days=-29)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],
                                 ["<Question: 2nd old>", "<Question: 1st old>"])


class DetailViewTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        future_question = create_question(question_text='future question',
                                          days=20)
        response = self.client.get(reverse('polls:detail',
                                           args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        past_question= create_question(question_text='past question',
                                       days=-20)
        response = self.client.get(reverse('polls:detail',
                                           args=(past_question.id,)))
        self.assertContains(response, past_question.question_text, status_code=200)
