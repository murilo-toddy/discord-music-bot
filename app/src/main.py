import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("DISCORD_TOKEN"))
print("hello from docker")
