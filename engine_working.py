from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

url_path = os.getenv("URL_PATH")

engine = create_engine(url_path, echo=True)

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS alchemist (x int, y int)"))
    conn.execute(
        text("INSERT INTO alchemist (x, y) VALUES (:x, :y)"),
        [{"x": 5, "y": 7},
        {"x": 1, "y": 3},
        {"x": 8, "y": 10}]
        )
    conn.commit()

