import re 
from tqdm import tqdm
data_path_c = "./data/invalid_email.csv"
data_path_b = "./data/valid_email.csv"
data_path = "./data/email.csv"
def mail_checker(user_email):
    user_email1 = re.match(pattern=r"(\w+\.?)*\+?\w+\@\w+\.\w+",string=str(user_email))
    if user_email1 is None:
        with open(data_path_c,'a') as csv:
         n = csv.write(f'{user_email}')   
    else:
        with open(data_path_b,'a') as csv:
            y = csv.write(f'{user_email}')
        

with open(data_path,'r') as csv:
    user_email = csv.readlines()
    for email in tqdm(user_email, desc="Generating emails"):
        mail_checker(email)

print(f"✅ Finish checking emails")