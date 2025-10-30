import re 
#def get_user_input(string_to_display):
    #a = input(string_to_display).strip()
    #return a 
data_path_b = "./data/valid_email.csv"
data_path = "./data/email.csv"
def mail_checker(user_email):
    user_email1 = re.match(pattern=r"(\w+\.?)*\+?\w+\@\w+\.\w+",string=str(user_email))
    if user_email1 is None:
        print("it didnt match")
        with open(data_path_b,'a') as csv:
         n = csv.write(f'{user_email} \n')   
    else:
        print("It has matched")
        with open(data_path,'a') as csv:
            y = csv.write(f'{user_email} \n')
        

with open(data_path,'r') as csv:
    user_email = csv.readlines()
    for user_email in user_email:
        mail_checker(user_email)
        print(user_email)               