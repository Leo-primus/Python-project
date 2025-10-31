from faker import Faker
from tqdm import tqdm

fake = Faker()
csv_path = "./data/email.csv"

# Use append mode to write as we go instead of storing in memory
with open(csv_path, 'w') as csv:
    for _ in tqdm(range(1_000_000), desc="Generating emails"):
        csv.write(fake.email() + '\n')

print(f"✅ Finished generating 1,000,000 emails at {csv_path}")
