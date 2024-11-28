# server/models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from server.common import Base
from datetime import datetime
from typing import Optional

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    image = Column(String)  # Добавлено поле image

class UserResponse(BaseModel):
    id: int
    email: str
    password: str
    image: str  # Добавлено поле image

    class Config:
        from_attributes = True

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    date_post = Column(DateTime)
    author = Column(String)
    image = Column(String)  # Добавлено поле image

class NewsResponse(BaseModel):
    id: Optional[int]
    title: str
    description: str
    date_post: Optional[datetime]  # Сделано опциональным
    author: str
    image: Optional[str]  # Сделано опциональным

    class Config:
        from_attributes = True

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)  # Добавлено поле image

class CompanyResponse(BaseModel):
    id: int
    name: str
    description: str
    image: str  # Добавлено поле image

    class Config:
        from_attributes = True

class Vacancy(Base):
    __tablename__ = "vacancies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    experience = Column(String)
    id_company = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company")
    image = Column(String)  # Добавлено поле image

class VacancyResponse(BaseModel):
    id: int
    name: str
    experience: str
    id_company: int
    image: str  # Добавлено поле image

    class Config:
        from_attributes = True

class EducationCompany(Base):
    __tablename__ = "education_companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)  # Добавлено поле image

class EducationCompanyResponse(BaseModel):
    id: int
    name: str
    description: str
    image: str  # Добавлено поле image

    class Config:
        from_attributes = True

class CourseEducation(Base):
    __tablename__ = "course_education"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    experience = Column(String)
    image = Column(String)  # Добавлено поле image

class CourseEducationResponse(BaseModel):
    id: int
    title: str
    experience: str
    image: str  # Добавлено поле image

    class Config:
        from_attributes = True

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(String)
    date = Column(DateTime)
    count_people = Column(Integer)
    city = Column(String)
    count_day_to_start = Column(Integer)
    image = Column(String)  # Добавлено поле image

class EventResponse(BaseModel):
    id: int
    title: str
    status: str
    date: datetime
    count_people: int
    city: str
    count_day_to_start: int
    image: str  # Добавлено поле image

    class Config:
        from_attributes = True