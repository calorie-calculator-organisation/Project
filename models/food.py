from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from sqlalchemy import String, ForeignKey
from .associates import user_food_assoc_table
from .base import Base




class Food:
    __tablename__='food'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    calories: Mapped[int] = mapped_column(String(100), nullable=False)
    fat: Mapped[Optional[int]] = mapped_column(String(50), nullable=False)
    protein: Mapped[Optional[int]] = mapped_column(String(50), nullable=False)
    carbs: Mapped[Optional[int]] = mapped_column(String(50), nullable=False)
    sugar: Mapped[Optional[int]] = mapped_column(String(50), nullable=False)


    


    