import unittest
from app.models import News
class NewsTest(unittest.TestCase) :
    def setUp(self):
        self.new_news = News('')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))   