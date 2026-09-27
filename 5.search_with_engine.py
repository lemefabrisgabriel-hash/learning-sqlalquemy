from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

url_path = os.getenv("URL_PATH")

engine = create_engine(url_path, echo=True)


with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM alchemist"))
    for row in result:
#        print(f"x: {row.x}, y: {row.y}")
        print(row)
