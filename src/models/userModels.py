from sqlalchemy import Column, Integer, String
from src.db.index import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)

    last_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
