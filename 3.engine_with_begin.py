from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

url_path = os.getenv("URL_PATH")

engine = create_engine(url_path, echo=True)

with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO alchemist (x, y) VALUES (:x, :y)"),
        [{"x":8, "y":15},
         {"x":10, "y":19},
         {"x":15, "y":29}],
    )

