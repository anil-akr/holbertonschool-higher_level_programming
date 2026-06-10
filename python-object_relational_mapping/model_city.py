#!/usr/bin/python3
"""Module that defines the City class mapped to the cities table."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Class City that maps to the cities table in the database"""
    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                unique=True,
                autoincrement=True)

    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False)
