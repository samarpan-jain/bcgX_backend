import uuid
from sqlalchemy import Column, String, DateTime
from core.database import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = "users"
    id = Column(String(255), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(150))
    email = Column(String(150), unique=True, index=True, nullable=False)
    role = Column(String(50))
    password = Column(String(150))
    created_at = Column(DateTime, default=lambda:datetime.now(timezone.utc))