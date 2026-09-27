from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

url_path = os.getenv("URL_PATH")

engine = create_engine(url_path, echo=True)

'''
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM alchemist WHERE y > :y"), {"y" : 0})
    for row in result:
        print(f"x: {row.x}, y: {row.y}")
'''

with engine.connect() as conn:
    sql = text("SELECT x, y FROM alchemist WHERE x > :x AND y > :y")
    x = input("x deve ser maior que...: ")
    y = input("y musst be greater than...: ")
    result = conn.execute(sql, {"x":x, "y":y})

    for row in result:
        print(f"x: {row.x}, y: {row.y}")

