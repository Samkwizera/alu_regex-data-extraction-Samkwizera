import re

email_pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
url_pattern = re.compile(r"^https?:\/\/(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}\/?.*$")
phone_pattern = re.compile(r"^\(?\d{3}\)?[-.]?\s?\d{3}[-.]?\s?\d{4}$")
credit_card_pattern = re.compile(r"^(\d{4}[-\s]){3}\d{4}$")
