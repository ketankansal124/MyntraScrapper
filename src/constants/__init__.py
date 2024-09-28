from dotenv import load_dotenv
import os

load_dotenv()


MONGODB_URL_KEY: str = os.getenv("MONGO_DB_URL")
MONGO_DATABASE_NAME: str = os.getenv("MONGO_DATABASE_NAME")
SESSION_PRODUCT_KEY: str = os.getenv("SESSION_PRODUCT_KEY")