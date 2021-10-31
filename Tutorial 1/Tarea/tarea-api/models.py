from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base #Se importa el objeto Base desde el archivo database.py

class News(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    url = Column(String(50))
    date = Column(String(50))
    media_outlet = Column(String(50))

    category = relationship("Category", back_populates="news")

class Category(Base):

    __tablename__ = "has_category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    news_id = Column(Integer, ForeignKey("news.id"))