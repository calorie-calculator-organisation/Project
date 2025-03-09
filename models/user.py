from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from sqlalchemy import String, ForeignKey
from .food import Food  
from .associates import user_food_assoc_table
from .base import Base

class User(Base):
    __tablename__='user'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[Optional[str]] = mapped_column(String(50))

    cart: Mapped[Optional[Food]] = relationship(secondary=user_food_assoc_table, back_populates="food_user")
