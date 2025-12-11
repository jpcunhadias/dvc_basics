import pandas as pd
from faker import Faker
import os

# Create a directory for the data
os.makedirs("data", exist_ok=True)

# Initialize Faker
fake = Faker()

# Generate fake data
data = {
    "name": [fake.name() for _ in range(100)],
    "email": [fake.email() for _ in range(100)],
    "address": [fake.address() for _ in range(100)],
    "text": [fake.text() for _ in range(100)],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("data/data.csv", index=False)

print("Fake data generated and saved to data/data.csv")
