import os
from dotenv import load_dotenv


load_dotenv()

ATLAS_USER = os.getenv("ATLAS_USER")
ATLAS_PASS = os.getenv("ATLAS_PASS")

mongo_url=f"mongodb+srv://{ATLAS_USER}:{ATLAS_PASS}@bdmlpt2501.62jmk.mongodb.net/"