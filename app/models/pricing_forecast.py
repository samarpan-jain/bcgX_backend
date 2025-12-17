from core.database import Base
from sqlalchemy import Column, String, BigInteger, ForeignKey, Float
from datetime import datetime, timezone
from sqlalchemy import DateTime

class PricingForecast(Base):
    __tablename__ = "pricing_forecasts"
    product_id = Column(String(255), ForeignKey("products.id"), primary_key=True)
    demand_forecast = Column(BigInteger, nullable=False)
    optimized_price = Column(Float(10,2), nullable=False)
    created_at = Column(DateTime, default=lambda:datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda:datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))