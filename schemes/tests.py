from django.test import TestCase
from .models import Scheme

class SchemeTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Post model
    """
    
    def test_str(self):
        test_title = Scheme(title='A scheme')
        self.assertEqual(str(test_title), 'A scheme')
