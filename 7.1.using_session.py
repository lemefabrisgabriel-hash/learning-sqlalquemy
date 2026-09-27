from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv()

url_path = os.getenv("URL_PATH")

engine = create_engine(url_path, echo=True)

with Session(engine) as session:
    session.add()
    session.add()
