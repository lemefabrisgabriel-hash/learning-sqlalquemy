from sqlalchemy import Table, Column, Integer, String, create_engine, text, ForeignKey
from dotenv import load_dotenv
import os

from metadata import metadata_obj

load_dotenv()

url_path = os.getenv("URL_PATH")

engine = create_engine(url_path, echo=True)

adress_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String(60), nullable=False),
)
metadata_obj.create_all(engine)

