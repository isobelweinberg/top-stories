import unittest
from src.scrape import get_headlines
from unittest.mock import patch

class TestHeadlines(unittest.TestCase):
    @patch("src.scrape.load_html")
    def test_headlines_list_from_mock_html(self, mock_load_html):
        
        with open("tests/bbc_homepage.html", "r", encoding="utf-8") as file:
            mock_html = file.read()

        mock_load_html.return_value = mock_html
        headlines = get_headlines()
   
        # Check that headlines is a list
        self.assertIsInstance(headlines, list, "Headlines should be a list")
        
        # Check that the list has exactly 5 items
        self.assertEqual(len(headlines), 5, "Headlines list should have 5 items")
        
        # Check that all items in the list are strings
        self.assertTrue(all(isinstance(headline, str) for headline in headlines), "All items in the headlines list should be strings")

    def test_headlines_list_from_live_code(self):
        
        headlines = get_headlines()
   
        # Check that headlines is a list
        self.assertIsInstance(headlines, list, "Headlines should be a list")
        
        # Check that the list has exactly 5 items
        self.assertEqual(len(headlines), 5, "Headlines list should have 5 items")
        
        # Check that all items in the list are strings
        self.assertTrue(all(isinstance(headline, str) for headline in headlines), "All items in the headlines list should be strings")

if __name__ == "__main__":
    unittest.main()
