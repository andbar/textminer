import re

def phone_number(text_string):
    match = re.findall(r"\(\d{3}\)\s\d{3}-\d{4}", text_string)
    if match:
        return match
