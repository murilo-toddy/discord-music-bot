import os
from dotenv import load_dotenv


if os.path.isfile(".env"):
    load_dotenv()

authentication = {key: value for key, value in os.environ.items()}

