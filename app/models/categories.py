from core.database import Base
from sqlalchemy import Column, String
import uuid
from sqlalchemy import DateTime
from datetime import datetime, timezone

class Category(Base):
    __tablename__ = "categories"
    id = Column(String(255), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(150), unique=True, index=True, nullable=False)
    description = Column(String(256))
    created_at = Column(DateTime, default=lambda:datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda:datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))