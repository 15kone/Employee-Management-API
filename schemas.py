from pydantic import BaseModel


class EmployeeBase(BaseModel):
    fullname: str
    email: str
    salary: float
    role: str
    phone: str
    is_active: bool


class EmployeeCreate(EmployeeBase):
    password: str

    class Config:
        exclude = ["hashed_password"]


class Employee(EmployeeBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "qkqgG@example.com",
                "role": "admin",
                "phone": "1234567890",
                "salary": 50000,
                "is_active": True,
            }
        }
