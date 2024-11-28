# server/services.py
import os
from sqlalchemy.orm import Session
from server.models import *
from fastapi import UploadFile

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app import config

DATABASE_URL = config.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Путь к папке с изображениями
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "images")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(db: Session, user: User):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse.from_orm(db_user)

def get_users(db: Session, user_id: int = None, email: str = None, password: str = None):
    query = db.query(User)
    if user_id:
        query = query.filter(User.id == user_id)
    if email:
        query = query.filter(User.email == email)
    if password:
        query = query.filter(User.password == password)
    return [UserResponse.from_orm(user) for user in query.all()]

async def upload_image(file: UploadFile):
    file_path = os.path.join(IMAGES_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    return file_path

def create_news(db: Session, news: News):
    db_news = News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return NewsResponse.from_orm(db_news)

def get_news(db: Session, news_id: int = None, title: str = None):
    query = db.query(News)
    if news_id:
        query = query.filter(News.id == news_id)
    if title:
        query = query.filter(News.title == title)
    return [NewsResponse.from_orm(news) for news in query.all()]

def create_company(db: Session, company: Company):
    db_company = Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return CompanyResponse.from_orm(db_company)

def get_companies(db: Session, company_id: int = None, name: str = None):
    query = db.query(Company)
    if company_id:
        query = query.filter(Company.id == company_id)
    if name:
        query = query.filter(Company.name == name)
    return [CompanyResponse.from_orm(company) for company in query.all()]

def create_vacancy(db: Session, vacancy: Vacancy):
    db_vacancy = Vacancy(**vacancy.dict())
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return VacancyResponse.from_orm(db_vacancy)

def get_vacancies(db: Session, vacancy_id: int = None, name: str = None):
    query = db.query(Vacancy)
    if vacancy_id:
        query = query.filter(Vacancy.id == vacancy_id)
    if name:
        query = query.filter(Vacancy.name == name)
    return [VacancyResponse.from_orm(vacancy) for vacancy in query.all()]

def create_education_company(db: Session, education_company: EducationCompany):
    db_education_company = EducationCompany(**education_company.dict())
    db.add(db_education_company)
    db.commit()
    db.refresh(db_education_company)
    return EducationCompanyResponse.from_orm(db_education_company)

def get_education_companies(db: Session, education_company_id: int = None, name: str = None):
    query = db.query(EducationCompany)
    if education_company_id:
        query = query.filter(EducationCompany.id == education_company_id)
    if name:
        query = query.filter(EducationCompany.name == name)
    return [EducationCompanyResponse.from_orm(education_company) for education_company in query.all()]

def create_course_education(db: Session, course_education: CourseEducation):
    db_course_education = CourseEducation(**course_education.dict())
    db.add(db_course_education)
    db.commit()
    db.refresh(db_course_education)
    return CourseEducationResponse.from_orm(db_course_education)

def get_course_educations(db: Session, course_education_id: int = None, title: str = None):
    query = db.query(CourseEducation)
    if course_education_id:
        query = query.filter(CourseEducation.id == course_education_id)
    if title:
        query = query.filter(CourseEducation.title == title)
    return [CourseEducationResponse.from_orm(course_education) for course_education in query.all()]

def create_event(db: Session, event: Event):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return EventResponse.from_orm(db_event)

def get_events(db: Session, event_id: int = None, title: str = None):
    query = db.query(Event)
    if event_id:
        query = query.filter(Event.id == event_id)
    if title:
        query = query.filter(Event.title == title)
    return [EventResponse.from_orm(event) for event in query.all()]