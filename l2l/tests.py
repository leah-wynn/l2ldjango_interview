from django.test import TestCase

from datetime import datetime
from l2l.templates.templatetags.l2l_extras import format_date

class FormatDateFilterTests(TestCase):

    def test_format_date_with_datetime(self):
        date = datetime(2024, 7, 16, 14, 30, 0)
        self.assertEqual(format_date(date), "2024-07-16 14:30:00")

    def test_format_date_with_string(self):
        date = datetime(2024, 7, 16, 14, 30, 0)
        string_datetime = date.strftime("%Y-%m-%dT%H:%M:%S")
        self.assertEqual(format_date(string_datetime), "2024-07-16 14:30:00")

    def test_format_date_with_non_date_string_returns_string(self):
        self.assertEqual(format_date("laskdjglsdnfladsk"), "laskdjglsdnfladsk")
