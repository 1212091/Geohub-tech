"""Model for user service"""

# pylint: disable=too-few-public-methods

from datetime import datetime

from pydantic import BaseModel, Field


class UserIn(BaseModel):
    """User input request class"""
    first_name: str = Field(
        ...,
        title="First name of user",
        example="John",
    )
    last_name: str = Field(
        ...,
        title="Last name of user",
        example="Snow",
    )
    phone: str = Field(
        ...,
        title="Phone number of user",
        example="0123456",
    )
    email: str = Field(
        ...,
        title="Email address of user",
        example="snow@gmail.com",
    )
    address: str = Field(
        ...,
        title="Address of user",
        example="456 Wall Street",
    )
    role_id: int = Field(
        ...,
        title="Role (by id) of user",
        example="1",
    )


class UserOut(UserIn):
    """User output request class"""
    id: int = Field(
        ...,
        title="Id of user",
        example="1",
    )


class UserRoleIn(BaseModel):
    """User role input request class"""
    role_name: str = Field(
        ...,
        title="Name of user role",
        example="Customer",
    )


class UserRoleOut(UserRoleIn):
    """User role output request class"""
    id: int = Field(
        ...,
        title="User role id",
        example="1",
    )


class UserActivityIn(BaseModel):
    """User activity input request class"""
    user_id: int = Field(
        ...,
        title="User id",
        example="1",
    )
    action: str = Field(
        ...,
        title="User action in website: search / filter / sort",
        example="sort by: code asc | filter_by: name",
    )


class UserActivity(UserActivityIn):
    """User activity model to persist to database"""
    timestamp: datetime = Field(
        ...,
        title="Time that user do action",
        example="2022-01-19 03:14:07",
    )


class UserActivityOut(UserActivityIn):
    """User acitivity output response class"""
    timestamp: datetime = Field(
        ...,
        title="Time that user do action",
        example="2022-01-19 03:14:07",
    )
    id: int = Field(
        ...,
        title="User activity id",
        example="1",
    )
