import unittest
from src.scrape import get_headlines

class TestHeadlines(unittest.TestCase):
    def test_headlines_list(self):

        headlines = get_headlines()
                
        # Check that headlines is a list
        self.assertIsInstance(headlines, list, "Headlines should be a list")
        
        # Check that the list has exactly 5 items
        self.assertEqual(len(headlines), 5, "Headlines list should have 5 items")
        
        # Check that all items in the list are strings
        self.assertTrue(all(isinstance(headline, str) for headline in headlines), "All items in the headlines list should be strings")

if __name__ == "__main__":
    unittest.main()
