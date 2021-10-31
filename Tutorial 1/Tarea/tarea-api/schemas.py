from typing import List, Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    news_id: int

    class Config:
        orm_mode = True


class NewsBase(BaseModel):
    title: str


class NewsCreate(NewsBase):
    pass

class News(NewsBase):
    id: int
    url: str
    date: str
    media_outlet: str
    categories: List[Category] = []

    class Config:
        orm_mode = True