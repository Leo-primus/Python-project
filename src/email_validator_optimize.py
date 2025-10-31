import re
import time
from tqdm import tqdm
# File paths
file_path_to_invalid = "./data/invalid_email.csv"
file_path_to_valid = "./data/valid_email.csv"
file_path_to_input_data = "./data/email.csv"

# Precompile regex once
email_pattern = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

# Lists to store results
invalid_emails = []
valid_emails = []

def mail_checker(user_email: str):
    """Check if an email is valid using precompiled regex."""
    if email_pattern.match(user_email):
        valid_emails.append(user_email)
    else:
        invalid_emails.append(user_email)

# Process file line-by-line
t1 = time.time()

with open(file_path_to_input_data, 'r', encoding='utf-8') as f:
    email_1 = f.readlines()
    for email in tqdm(email_1, desc="Generating emails"):
        if email:  # skip empty lines
            mail_checker(email)

print(f"Processing took {time.time() - t1:.4f} seconds")

# Write results (one per line)
with open(file_path_to_invalid, 'w', encoding='utf-8') as f_invalid:
    f_invalid.write("\n".join(invalid_emails))

with open(file_path_to_valid, 'w', encoding='utf-8') as f_valid:
    f_valid.write("\n".join(valid_emails))

print(f"✅ Finish checking emails")