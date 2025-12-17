from core.database import Base
from sqlalchemy import Column, String, BigInteger, ForeignKey, DateTime
from datetime import datetime, timezone

class CustomerRating(Base):
    __tablename__ = "customer_ratings"
    product_id = Column(String(255), ForeignKey("products.id"), primary_key=True)
    rating = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, default=lambda:datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda:datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
