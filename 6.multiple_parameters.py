from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

url_path = os.getenv("URL_PATH")

engine = create_engine(url_path, echo=True)

with engine.connect() as conn:
    sql = text("INSERT INTO alchemist (x, y) VALUES (:x, :y)")
    
    conn.execute(sql,
                 [{"x": 3, "y": 29}, {"x": 2, "y": 19}, {"x": 7, "y": 69}],
    )
    conn.commit()


#    sql = text("DELETE FROM alchemist WHERE (x = 3 AND y = 29) OR (x = 2 AND y = 19) OR (x = 7 AND y = 69)")
#    conn.execute(sql)
#    conn.commit()


    sql_look = text("SELECT x, y FROM alchemist")

    result = conn.execute(sql_look)
    for row in result:
        print(f"x: {row.x}, y: {row.y}")

