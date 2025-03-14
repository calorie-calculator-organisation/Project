from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from sqlalchemy import String, Integer
from .food import Food  
from .associates import user_food_assoc_table
from .base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    cart: Mapped[List["Food"]] = relationship("Food", secondary=user_food_assoc_table, back_populates="users")