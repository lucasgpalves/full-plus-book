from typing import List

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.note import Note

class Book(Base):
    __tablename__ = "book_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=True)
    atual_pages = Column(Integer, nullable=True)
    pages = Column(Integer, nullable=False)
    notes: Mapped[List["Note"]] = relationship()
    daily_reading_activities: Mapped[List["DailyReadingActivity"]] = relationship("DailyReadingActivity", back_populates="book")