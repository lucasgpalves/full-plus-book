from typing import List
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base

class Note(Base):
    __tablename__ = "note_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, default=datetime.now)    
    description = Column(String, nullable=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("book_table.id"))
    book: Mapped["Book"] = relationship("Book", back_populates="notes")