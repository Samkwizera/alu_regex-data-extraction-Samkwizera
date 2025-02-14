from extractors import (
    extract_emails,
    extract_urls,
    extract_phone_numbers,
    extract_credit_cards
)

def run_demo():
    sample_text = """
    user@example.com
    firstname.lastname@company.co.uk
    https://www.example.com
    http://subdomain.example.org/page
    (123) 456-7890
    123-456-7890
    123.456.7890
    1234-5678-9012-3456
    1234 5678 9012 3456
    """
    emails = extract_emails(sample_text)
    urls = extract_urls(sample_text)
    phones = extract_phone_numbers(sample_text)
    cards = extract_credit_cards(sample_text)

    print("Emails:", emails)
    print("URLs:", urls)
    print("Phone numbers:", phones)
    print("Credit cards:", cards)

if __name__ == "__main__":
    run_demo()
