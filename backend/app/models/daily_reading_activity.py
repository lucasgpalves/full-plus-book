from sqlalchemy import Column, Date, ForeignKey, Boolean
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from datetime import date

from app.models.base import Base

class DailyReadingActivity(Base):
    __tablename__ = "daily_reading_activity_table"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date = Column(Date, default=date.today, nullable=False)
    state = Column(Boolean, default=False, nullable=False)
    book_id: Mapped[int] = mapped_column(ForeignKey("book_table.id"))
    book: Mapped["Book"] = relationship("Book", back_populates="daily_reading_activities")