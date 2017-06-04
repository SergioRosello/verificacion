import unittest
from unittest import TestCase
from code.url_scrapper import Scrapper
import mock
import os


class TestScrapper(TestCase):

    @mock.patch('code.Scrapper.get_rss')
    def test_url_scrapper_parse_xml(self,mock_rss):
        # Setup: I will use a file with the list of titles similar to the real output to validate my function.
        # I read every line and save it in an array called 'result'
        with open(os.path.dirname(os.path.abspath(__file__)) + '/portada_result.txt') as f:
            content = f.readlines()
        result = [x.strip() for x in content]

        # I mock the output in a method I'm using to get rss. In this case I'm reading from a file
        mock_rss.return_value = open(os.path.dirname(os.path.abspath(__file__))+ '/../tests/portada.xml', 'r')

        # Execute the methods I want to test. In my case parse_xml
        scraper = Scrapper('http://fake.url')
        scraper.parse_xml()

        # Validate the result I get in scraper (list of titles) is equal to the result I read from the output_result file
        self.assertEqual(scraper.list_of_articles, result)

    @mock.patch('code.Scrapper.get_rss')
    def test_url_scrapper_check_date(self,mock_rss):
        # I mock the output in a method I'm using to get rss. In this case I'm reading from a file
        mock_rss.return_value = open(os.path.dirname(os.path.abspath(__file__))+ '/../tests/portada.xml', 'r')

        # Execute the methods I want to test. In my case check_date
        scraper = Scrapper('http://fake.url')
        date = scraper.check_date()

        # Validate the result I get in scraper (list of titles) is equal to the result I read from the output_result file
        self.assertEqual(date, 'Wed, 24 May 2017 20:47:28 +0200')

if __name__ == '__main__':
    unittest.main()