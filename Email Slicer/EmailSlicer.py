import re

def isValidEmail(email):

    # Regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    return bool((re.fullmatch(regex, email)))

email = input("Enter your email id - ")

if isValidEmail(email):
    username = email[:email.index('@')]
    domain = email[email.index('@')+1: ]
    print("Username - ", username)
    print("Domain - ", domain)
else:
    print("Invalid Email!")