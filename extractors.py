from patterns import (
    email_pattern,
    url_pattern,
    phone_pattern,
    credit_card_pattern
)

def extract_emails(text):
    return email_pattern.findall(text)

def extract_urls(text):
    return url_pattern.findall(text)

def extract_phone_numbers(text):
    return phone_pattern.findall(text)

def extract_credit_cards(text):
    return credit_card_pattern.findall(text)
