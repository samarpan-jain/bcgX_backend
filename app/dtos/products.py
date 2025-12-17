from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(max_length=150)
    description: str = Field(max_length=256)
    cost_price: float = Field(ge=1)
    selling_price: float = Field(ge=1)
    category: str
    stock_available: int = Field(ge=0)
    unit_sold: int = Field(ge=0)

class ProductRes(ProductBase):
    id: str

class ProductDTO(ProductBase):
    class Config:
        from_attributes = True