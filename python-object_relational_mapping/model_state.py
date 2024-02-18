#!/usr/bin/python3
"""Defines the State class and the declarative base for SQLAlchemy."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()


class State(Base):
    """Represents a state in the database."""

    # Table name in the database
    __tablename__ = 'states'

    # Columns in the table
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
