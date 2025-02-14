import unittest        # Import the unittest module   
from extractors import (
    extract_emails,
    extract_urls,
    extract_phone_numbers,
    extract_credit_cards
)
# Import the functions to be tested
class TestExtractors(unittest.TestCase):
    def test_extract_emails(self):
        text = "user@example.com firstname.lastname@company.co.uk"
        result = extract_emails(text)
        self.assertIn("user@example.com", result)
        self.assertIn("firstname.lastname@company.co.uk", result)
        self.assertEqual(len(result), 2)
# Test the extract_emails function
    def test_extract_urls(self):
        text = "http://subdomain.example.org/page https://www.example.com"
        result = extract_urls(text)
        self.assertEqual(len(result), 2)
# Test the extract_urls function
    def test_extract_phone_numbers(self):
        text = "(123) 456-7890 123-456-7890 123.456.7890"
        result = extract_phone_numbers(text)
        self.assertEqual(len(result), 3)
#   Test the extract_phone_numbers function
    def test_extract_credit_cards(self):
        text = "1234-5678-9012-3456 1234 5678 9012 3456"
        result = extract_credit_cards(text)
        self.assertEqual(len(result), 2)
# Test the extract_credit_cards function
if __name__ == '__main__':
    unittest.main()
# Run the tests if the script is run directly  from the command line 