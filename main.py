# main.py
import os
import sqlite3
import uvicorn
from fastapi import FastAPI, Depends, UploadFile, File, Query
from sqlalchemy.orm import Session
from src.app import config
from server.models import Base
from server.services import *

app = FastAPI(
    title="ИТ навигатор"
)

# Создаем таблицы при запуске приложения
DATABASE_URL = config.DATABASE_URL
engine = create_engine(DATABASE_URL)

def init_db():
    Base.metadata.create_all(bind=engine)
    load_initial_data()

def load_initial_data():
    conn = sqlite3.connect(DATABASE_URL.replace('sqlite:///', ''))
    cursor = conn.cursor()
    with open('server/init.sql', 'r') as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()
    conn.close()

init_db()



@app.post("/users/", response_model=UserResponse)
def create_user_endpoint(
    user: UserResponse, 
    db: Session = Depends(get_db)
):
    return create_user(db, user)

@app.get("/users/", response_model=list[UserResponse])
def get_users_endpoint(
    user_id: int = Query(None), 
    email: str = Query(None), 
    db: Session = Depends(get_db), 
    password: str = Query(None)
):
    return get_users(db, user_id, email, password)

@app.post("/news/", response_model=NewsResponse)
def create_news_endpoint(
    news: NewsResponse, 
    db: Session = Depends(get_db)
):
    return create_news(db, news)

@app.get("/news/", response_model=list[NewsResponse])
def get_news_endpoint(
    news_id: int = Query(None), 
    title: str = Query(None), 
    db: Session = Depends(get_db)
):
    return get_news(db, news_id, title)

@app.post("/companies/", response_model=CompanyResponse)
def create_company_endpoint(
    company: CompanyResponse, 
    db: Session = Depends(get_db)
):
    return create_company(db, company)

@app.get("/companies/", response_model=list[CompanyResponse])
def get_companies_endpoint(
    company_id: int = Query(None), 
    name: str = Query(None), 
    db: Session = Depends(get_db)
):
    return get_companies(db, company_id, name)

@app.post("/vacancies/", response_model=VacancyResponse)
def create_vacancy_endpoint(
    vacancy: VacancyResponse, 
    db: Session = Depends(get_db)
):
    return create_vacancy(db, vacancy)

@app.get("/vacancies/", response_model=list[VacancyResponse])
def get_vacancies_endpoint(
    vacancy_id: int = Query(None), 
    name: str = Query(None), 
    db: Session = Depends(get_db)
):
    return get_vacancies(db, vacancy_id, name)

@app.post("/education-companies/", response_model=EducationCompanyResponse)
def create_education_company_endpoint(
    education_company: EducationCompanyResponse, 
    db: Session = Depends(get_db)
):
    return create_education_company(db, education_company)

@app.get("/education-companies/", response_model=list[EducationCompanyResponse])
def get_education_companies_endpoint(
    education_company_id: int = Query(None), 
    name: str = Query(None), 
    db: Session = Depends(get_db)
):
    return get_education_companies(db, education_company_id, name)

@app.post("/courses-education/", response_model=CourseEducationResponse)
def create_course_education_endpoint(
    course_education: CourseEducationResponse, 
    db: Session = Depends(get_db)
):
    return create_course_education(db, course_education)

@app.get("/courses-education/", response_model=list[CourseEducationResponse])
def get_course_educations_endpoint(
    course_education_id: int = Query(None), 
    title: str = Query(None), 
    db: Session = Depends(get_db)
):
    return get_course_educations(db, course_education_id, title)

@app.post("/events/", response_model=EventResponse)
def create_event_endpoint(
    event: EventResponse, 
    db: Session = Depends(get_db)
):
    return create_event(db, event)

@app.get("/events/", response_model=list[EventResponse])
def get_events_endpoint(
    event_id: int = Query(None), 
    title: str = Query(None), 
    db: Session = Depends(get_db)
):
    return get_events(db, event_id, title)

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=config.API_HOST,
        port=config.API_PORT
    )