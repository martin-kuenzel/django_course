from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse
from polls.models import Poll

# Create your tests here.
class PollModelTests(TestCase):
    def test_was_published_recently_with_future_poll(self):
        """ 
        was_published_recently() returns True for date_created of poll lies in the future, 
        """
        p = Poll(date_created=timezone.now() + datetime.timedelta(30))
        self.assertIs( p.was_published_recently(), False )

    def test_was_published_recently_with_old_poll(self):
        """
        was_published_recently() returns False for polls whose date_created
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_poll = Poll(date_created=time)
        self.assertIs(old_poll.was_published_recently(), False)

    def test_was_published_recently_with_recent_poll(self):
        """
        was_published_recently() returns True for polls whose date_created
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_poll = Poll(date_created=time)
        self.assertIs(recent_poll.was_published_recently(), True)


def create_poll(title, days):
    """
    Create a poll with the given `title` and published the
    given number of `days` offset to now (negative for polls published
    in the past, positive for polls that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Poll.objects.create(title=title, date_created=time)


class PollIndexViewTests(TestCase):
    def test_no_polls(self):
        """
        If no polls exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls-index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['polls'], [])

    def test_past_poll(self):
        """
        Polls with a date_created in the past are displayed on the
        index page.
        """
        create_poll(title="Past poll.", days=-30)
        response = self.client.get(reverse('polls-index'))
        self.assertQuerysetEqual(
            response.context['polls'],
            ['<Poll: Past poll.>']
        )

    def test_future_poll(self):
        """
        Polls with a date_created in the future aren't displayed on
        the index page.
        """
        create_poll(title="Future poll.", days=30)
        response = self.client.get(reverse('polls-index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['polls'], [])

    def test_future_poll_and_past_poll(self):
        """
        Even if both past and future polls exist, only past polls
        are displayed.
        """
        create_poll(title="Past poll.", days=-30)
        create_poll(title="Future poll.", days=30)
        response = self.client.get(reverse('polls-index'))
        self.assertQuerysetEqual(
            response.context['polls'],
            ['<Poll: Past poll.>']
        )

    def test_two_past_polls(self):
        """
        The polls index page may display multiple polls.
        """
        create_poll(title="Past poll 1.", days=-30)
        create_poll(title="Past poll 2.", days=-5)
        response = self.client.get(reverse('polls-index'))
        self.assertQuerysetEqual(
            response.context['polls'],
            ['<Poll: Past poll 2.>', '<Poll: Past poll 1.>']
        )

class PollDetailViewTests(TestCase):
    def test_future_poll(self):
        """
        The detail view of a poll with a date_created in the future
        returns a 404 not found.
        """
        future_poll = create_poll(title='Future poll.', days=5)
        url = reverse('poll-details', args=(future_poll.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_poll(self):
        """
        The detail view of a poll with a date_created in the past
        displays the poll's text.
        """
        past_poll = create_poll(title='Past Poll.', days=-5)
        url = reverse('poll-details', args=(past_poll.id,))
        response = self.client.get(url)
        self.assertContains(response, past_poll.title)


class PollResultsViewTests(TestCase):
    def test_future_poll(self):
        """
        The detail view of a poll with a date_created in the future
        returns a 404 not found.
        """
        future_poll = create_poll(title='Future poll.', days=5)
        url = reverse('poll-results', args=(future_poll.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_poll(self):
        """
        The detail view of a poll with a date_created in the past
        displays the poll's text.
        """
        past_poll = create_poll(title='Past Poll.', days=-5)
        url = reverse('poll-results', args=(past_poll.id,))
        response = self.client.get(url)
        self.assertContains(response, past_poll.title)