from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

url_path = os.getenv("URL_PATH")

engine = create_engine(url_path, echo=True)

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String(100))
    )

metadata_obj.create_all(engine)

with engine.connect() as conn:
    sql = text("SELECT * FROM user_account")
    result = conn.execute(sql)
    for row in result:
        print(row)

