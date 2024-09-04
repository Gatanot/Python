import re
phone_number_regex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_number_regex.search("my number is 415-555-4242")
print("phone number found: "+mo.group())