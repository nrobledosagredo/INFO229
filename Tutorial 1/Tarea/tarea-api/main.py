from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/v1/news/", response_model=schemas.News)
def create_news(news: schemas.NewsCreate, db: Session = Depends(get_db)):

    return crud.create_news(db=db, news=news)


@app.get("/v1/news/", response_model=List[schemas.News])
def read_news(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = crud.get_news(db, skip=skip, limit=limit)
    return news


@app.get("/v1/news/{news_id}", response_model=schemas.News)
def read_news(news_id: int, db: Session = Depends(get_db)):
    db_news = crud.get_news(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news


@app.post("/v1/news/{news_id}/category/", response_model=schemas.Category)
def create_category_for_news(
    news_id: int, Category: schemas.CategoryCreate, db: Session = Depends(get_db)
):
    return crud.create_category(db=db, category=category, news_id=news_id)


@app.get("/v1/categories/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_categories(db, skip=skip, limit=limit)
    return categories