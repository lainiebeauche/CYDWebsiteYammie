from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Message(Base):
    """Represents a simple textual message from a user."""
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    text = Column(String)
