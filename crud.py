from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
import schemas


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employee_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    fake_hashed_password = employee.password + "notreallyhashed"
    db_employee = models.Employee(
        email=employee.email,
        # hashed_password=fake_hashed_password,
        fullname=employee.fullname,
        role=employee.role,
        phone=employee.phone,
        salary=employee.salary,
        is_active=employee.is_active,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db, employee_id):
    db_employee = (
        db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    )
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()
    return db_employee


def update_employee(
    db: Session,
    employee_id: int,
    full_name: str = None,
    email: str = None,
    salary: float = None,
    role: str = None,
    phone: str = None,
    is_active: bool = None,
):
    employee = (
        db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    )
    if employee:
        if full_name is not None:
            employee.full_name = full_name
        if email is not None:
            employee.email = email
        if salary is not None:
            employee.salary = salary
        if role is not None:
            employee.role = role
        if phone is not None:
            employee.phone = phone
        if is_active is not None:
            employee.is_active = is_active
        db.commit()
        db.refresh(employee)
        return employee
    else:
        return None


def apply_raise(db: Session, employee_id: int):
    employee = (
        db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    )
    if employee:
        employee.salary = employee.salary * 1.05
        db.commit()
        db.refresh(employee)
        return employee
    else:
        raise HTTPException(status_code=404, detail="Employee not found")
