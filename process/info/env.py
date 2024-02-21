import os
from dotenv import load_dotenv # pip install python-dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables using os.getenv()
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG")

# Use the variables in your script
print("Database URL:", database_url)
print("API Key:", api_key)
print("Debug Mode:", debug_mode)


# Retrieving the value of the "PATH" environment variable
path = os.environ["PATH"]
print(path)

database_url = os.environ.get("DATABASE_URL", "localhost:5432")
print(database_url)

# Setting a new environment variable
os.environ["API_KEY"] = "YOUR_API_KEY"