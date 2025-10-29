import re
def get_user_input(string_to_display):
    while True:
        a = input(string_to_display)
        

def mail_checker(user_email):
    user_email = re.match(pattern="(\w+[^@+]\w+)+(\W\w+\W\w+\W?\w+)" ,string=user_email)
    print(user_email)

while True:
    user_email = get_user_input("Please enter your Email address:")
    mail_checker(user_email)
