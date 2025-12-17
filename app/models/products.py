import uuid
from sqlalchemy import Column, String, Float, BigInteger, ForeignKey, DateTime
from core.database import Base
from datetime import datetime, timezone

class Products(Base):
    __tablename__ = "products"
    id = Column(String(255), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(150), unique=True, index=True, nullable=False)
    description = Column(String(256))
    cost_price = Column(Float(10,2))
    selling_price = Column(Float(10,2))
    category = Column(String(100), ForeignKey("categories.name"))
    stock_available = Column(BigInteger)
    unit_sold = Column(BigInteger)
    created_at = Column(DateTime, default=lambda:datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda:datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))