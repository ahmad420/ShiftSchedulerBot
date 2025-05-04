"""
Department model representing organizational departments.
"""
from typing import List, Optional

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import Base


class Department(Base):
    """
    Department model representing an organizational department.
    """
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)

    # Relationships
    users = relationship("User", back_populates="department")
    shifts = relationship("Shift", back_populates="department")

    def __repr__(self) -> str:
        """
        String representation of the department.
        """
        return f"<Department {self.name}>" 