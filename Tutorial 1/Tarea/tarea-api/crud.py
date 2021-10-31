from sqlalchemy.orm import Session

from . import models, schemas


def get_news(db: Session, news_id: int):
    return db.query(models.News).filter(models.News.id == news_id).first()

def get_news_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(mouser_iddels.News).offset(skip).limit(limit).all()

def create_news(db: Session, news: schemas.NewsCreate):
    db_news = models.News(title=news.title, url=news.url, date=news.date, media_outlet=news.media_outlet)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryCreate, news_id: int):
    db_category = models.Category(**category.dict(), news_id=news_id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category