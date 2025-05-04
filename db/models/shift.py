"""
Shift model representing work shifts.
"""
from datetime import datetime
from enum import Enum
from typing import List, Optional

from sqlalchemy import Column, DateTime, Enum as SQLEnum, ForeignKey, String
from sqlalchemy.orm import relationship

from .base import Base


class ShiftType(str, Enum):
    """
    Enum for shift types.
    """
    MORNING = "morning"
    EVENING = "evening"
    NIGHT = "night"


class Shift(Base):
    """
    Shift model representing a work shift.
    """
    date = Column(DateTime, nullable=False)
    shift_type = Column(SQLEnum(ShiftType), nullable=False)
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False)

    # Relationships
    department = relationship("Department", back_populates="shifts")
    assignments = relationship("ShiftAssignment", back_populates="shift")
    swap_requests = relationship("SwapRequest", back_populates="shift")

    def __repr__(self) -> str:
        """
        String representation of the shift.
        """
        return f"<Shift {self.date.date()} {self.shift_type}>" 