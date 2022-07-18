from pydantic import BaseModel

from datetime import datetime

class UserIn(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    address: str
    role_id: int
    
class UserOut(UserIn):
    id: int
    
class UserRoleIn(BaseModel):
    role_name: str
    
class UserRoleOut(UserRoleIn):
    id: int
    
class UserActivityIn(BaseModel):
    user_id: int
    action: str
    
class UserActivity(UserActivityIn):
    timestamp: datetime
    
class UserActivityOut(UserActivityIn):
    timestamp: datetime
    id: int