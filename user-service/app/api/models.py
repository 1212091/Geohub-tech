"""Model for user service"""

# pylint: disable=too-few-public-methods

from datetime import datetime

from pydantic import BaseModel


class UserIn(BaseModel):
    """User input request class"""
    first_name: str
    last_name: str
    phone: str
    email: str
    address: str
    role_id: int


class UserOut(UserIn):
    """User output request class"""
    id: int


class UserRoleIn(BaseModel):
    """User role input request class"""
    role_name: str


class UserRoleOut(UserRoleIn):
    """User role output request class"""
    id: int


class UserActivityIn(BaseModel):
    """User activity input request class"""
    user_id: int
    action: str


class UserActivity(UserActivityIn):
    """User activity model to persist to database"""
    timestamp: datetime


class UserActivityOut(UserActivityIn):
    """User acitivity output response class"""
    timestamp: datetime
    id: int
