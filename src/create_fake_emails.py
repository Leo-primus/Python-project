from faker import Faker
fake = Faker()
csv_path = "./data/email.csv"
for faker_names in range(1,1_000_000):
  with open(csv_path, 'a') as csv:
    emails = csv.write(f'{fake.email()} \n')