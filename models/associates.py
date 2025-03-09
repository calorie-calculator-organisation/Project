from sqlalchemy import Table, Column, Integer, ForeignKey

from .base import Base


user_food_assoc_table = Table(
    'user_food',
    Base.metadata,
    Column("user_id", Integer, ForeignKey('user.id'), primary_key=True),
    Column("food_id", Integer, ForeignKey("food.id"), primary_key=True),
)
