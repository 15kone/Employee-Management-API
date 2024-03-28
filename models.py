from sqlalchemy import Column, Integer, String, Boolean, Float

from database import Base


class Employee(Base):

    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    salary = Column(Float)
    role = Column(String)
    phone = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
